//
//  InputMethodView.swift
//  输入方式选择
//

import SwiftUI
import UniformTypeIdentifiers

struct InputMethodView: View {
    @ObservedObject var project: DesignProject
    @State private var selectedType: BoundaryType = .cad
    @State private var isDragging = false
    @State private var showFilePicker = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            // 输入方式选择
            Picker("输入方式", selection: $selectedType) {
                ForEach(BoundaryType.allCases, id: \.self) { type in
                    Label(type.rawValue, systemImage: type.icon)
                        .tag(type)
                }
            }
            .pickerStyle(SegmentedPickerStyle())
            .onChange(of: selectedType) { newType in
                project.inputData.boundaryType = newType
            }
            
            // 拖放区域
            ZStack {
                RoundedRectangle(cornerRadius: 12)
                    .fill(isDragging ? Color.accentColor.opacity(0.1) : Color.gray.opacity(0.1))
                    .overlay(
                        RoundedRectangle(cornerRadius: 12)
                            .stroke(isDragging ? Color.accentColor : Color.gray.opacity(0.3),
                                   style: StrokeStyle(lineWidth: 2, dash: [5]))
                    )
                
                VStack(spacing: 12) {
                    Image(systemName: selectedType.icon)
                        .font(.system(size: 48))
                        .foregroundColor(isDragging ? .accentColor : .gray)
                    
                    Text("拖放文件到此处")
                        .font(.headline)
                        .foregroundColor(.secondary)
                    
                    Text("或")
                        .font(.caption)
                        .foregroundColor(.secondary)
                    
                    Button("选择文件") {
                        showFilePicker = true
                    }
                    .buttonStyle(.bordered)
                }
                .padding(40)
            }
            .frame(height: 200)
            .onDrop(of: [.fileURL], isTargeted: $isDragging) { providers in
                handleDrop(providers: providers)
            }
            
            // 支持的格式说明
            HStack {
                Image(systemName: "info.circle")
                    .foregroundColor(.secondary)
                Text("支持格式: \(selectedType.fileExtensions.joined(separator: ", "))")
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            // 已导入文件预览
            if let fileURL = project.inputData.boundaryFile {
                ImportedFileView(fileURL: fileURL, onDelete: {
                    project.inputData.boundaryFile = nil
                    project.inputData.boundaryImage = nil
                })
            }
            
            // 图片预览
            if let image = project.inputData.boundaryImage {
                Image(nsImage: image)
                    .resizable()
                    .scaledToFit()
                    .frame(maxHeight: 300)
                    .cornerRadius(8)
            }
        }
        .fileImporter(
            isPresented: $showFilePicker,
            allowedContentTypes: contentTypes(for: selectedType),
            allowsMultipleSelection: false
        ) { result in
            handleFileImport(result: result)
        }
    }
    
    private func contentTypes(for type: BoundaryType) -> [UTType] {
        switch type {
        case .cad:
            return [UTType(filenameExtension: "dwg")!, UTType(filenameExtension: "dxf")!]
        case .image:
            return [.png, .jpeg, .tiff]
        case .gis:
            return [UTType(filenameExtension: "shp")!, UTType(filenameExtension: "geojson")!]
        }
    }
    
    private func handleDrop(providers: [NSItemProvider]) -> Bool {
        for provider in providers {
            provider.loadItem(forTypeIdentifier: UTType.fileURL.identifier, options: nil) { (urlData, error) in
                DispatchQueue.main.async {
                    if let urlData = urlData as? Data,
                       let url = URL(dataRepresentation: urlData, relativeTo: nil) {
                        processFile(url: url)
                    }
                }
            }
        }
        return true
    }
    
    private func handleFileImport(result: Result<[URL], Error>) {
        switch result {
        case .success(let urls):
            if let url = urls.first {
                processFile(url: url)
            }
        case .failure(let error):
            print("导入失败: \(error)")
        }
    }
    
    private func processFile(url: URL) {
        project.inputData.boundaryFile = url
        
        // 如果是图片，直接加载预览
        if selectedType == .image {
            if let image = NSImage(contentsOf: url) {
                project.inputData.boundaryImage = image
                // 解析图片获取边界（简化版）
                parseImageBoundary(image: image)
            }
        } else {
            // CAD或GIS文件，需要解析
            parseCADorGISFile(url: url)
        }
    }
    
    private func parseImageBoundary(image: NSImage) {
        // 简化版：使用图片尺寸作为边界
        let size = image.size
        project.inputData.boundaryPoints = [
            CGPoint(x: 0, y: 0),
            CGPoint(x: size.width, y: 0),
            CGPoint(x: size.width, y: size.height),
            CGPoint(x: 0, y: size.height)
        ]
        project.inputData.landArea = Double(size.width * size.height) / 10000.0 // 简化为公顷
    }
    
    private func parseCADorGISFile(url: URL) {
        // 实际项目中这里调用CAD/GIS解析库
        // 简化版：设置示例数据
        project.inputData.boundaryPoints = [
            CGPoint(x: 0, y: 0),
            CGPoint(x: 100, y: 0),
            CGPoint(x: 120, y: 80),
            CGPoint(x: 80, y: 100),
            CGPoint(x: 20, y: 90)
        ]
        project.inputData.landArea = 9900.0 // 约1公顷
    }
}

// MARK: - 已导入文件视图
struct ImportedFileView: View {
    let fileURL: URL
    let onDelete: () -> Void
    
    var body: some View {
        HStack {
            Image(systemName: "doc.fill")
                .foregroundColor(.accentColor)
            
            VStack(alignment: .leading, spacing: 4) {
                Text(fileURL.lastPathComponent)
                    .lineLimit(1)
                Text(fileURL.pathExtension.uppercased())
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            Spacer()
            
            Button(action: onDelete) {
                Image(systemName: "xmark.circle.fill")
                    .foregroundColor(.red)
            }
            .buttonStyle(.plain)
        }
        .padding()
        .background(Color.gray.opacity(0.1))
        .cornerRadius(8)
    }
}

// MARK: - 项目信息卡片
struct ProjectInfoCard: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Image(systemName: "folder.fill")
                    .foregroundColor(.accentColor)
                TextField("项目名称", text: $project.name)
                    .font(.headline)
            }
            
            Divider()
            
            HStack {
                Label("创建时间", systemImage: "calendar")
                    .font(.caption)
                    .foregroundColor(.secondary)
                Spacer()
                Text(project.createdAt, style: .date)
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            if project.inputData.landArea > 0 {
                HStack {
                    Label("用地面积", systemImage: "ruler")
                        .font(.caption)
                        .foregroundColor(.secondary)
                    Spacer()
                    Text(String(format: "%.2f ㎡", project.inputData.landArea))
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }
        }
        .padding()
        .background(Color.gray.opacity(0.1))
        .cornerRadius(12)
    }
}

// MARK: - 边界预览
struct BoundaryPreview: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Label("用地边界预览", systemImage: "map")
                .font(.headline)
            
            if !project.inputData.boundaryPoints.isEmpty {
                GeometryReader { geometry in
                    ZStack {
                        // 绘制边界
                        BoundaryShape(points: project.inputData.boundaryPoints)
                            .stroke(Color.accentColor, lineWidth: 2)
                            .background(
                                BoundaryShape(points: project.inputData.boundaryPoints)
                                    .fill(Color.accentColor.opacity(0.1))
                            )
                    }
                }
                .frame(height: 200)
                .background(Color.gray.opacity(0.05))
                .cornerRadius(8)
            }
            
            // 边界点信息
            HStack {
                Label("顶点数", systemImage: "pin")
                    .font(.caption)
                Spacer()
                Text("\(project.inputData.boundaryPoints.count)")
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
        }
        .padding()
        .background(Color.gray.opacity(0.1))
        .cornerRadius(12)
    }
}

// MARK: - 边界形状
struct BoundaryShape: Shape {
    let points: [CGPoint]
    
    func path(in rect: CGRect) -> Path {
        var path = Path()
        
        guard !points.isEmpty else { return path }
        
        // 计算边界框
        let minX = points.map { $0.x }.min() ?? 0
        let maxX = points.map { $0.x }.max() ?? 100
        let minY = points.map { $0.y }.min() ?? 0
        let maxY = points.map { $0.y }.max() ?? 100
        
        let scaleX = rect.width / CGFloat(maxX - minX)
        let scaleY = rect.height / CGFloat(maxY - minY)
        let scale = min(scaleX, scaleY) * 0.9
        
        let offsetX = (rect.width - CGFloat(maxX - minX) * scale) / 2
        let offsetY = (rect.height - CGFloat(maxY - minY) * scale) / 2
        
        // 绘制多边形
        if let first = points.first {
            let x = offsetX + CGFloat(first.x - minX) * scale
            let y = rect.height - (offsetY + CGFloat(first.y - minY) * scale)
            path.move(to: CGPoint(x: x, y: y))
            
            for point in points.dropFirst() {
                let x = offsetX + CGFloat(point.x - minX) * scale
                let y = rect.height - (offsetY + CGFloat(point.y - minY) * scale)
                path.addLine(to: CGPoint(x: x, y: y))
            }
            
            path.closeSubpath()
        }
        
        return path
    }
}
