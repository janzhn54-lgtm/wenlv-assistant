//
//  OutputGallery.swift
//  成果展示
//

import SwiftUI

struct OutputGallery: View {
    @ObservedObject var project: DesignProject
    @State private var selectedOutput: DesignOutput?
    
    let columns = [
        GridItem(.adaptive(minimum: 250))
    ]
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                // 生成状态
                GenerationStatusView(project: project)
                
                // 输出成果网格
                if !project.outputs.isEmpty {
                    LazyVGrid(columns: columns, spacing: 20) {
                        ForEach(project.outputs) { output in
                            OutputCard(output: output)
                                .onTapGesture {
                                    selectedOutput = output
                                }
                        }
                    }
                } else {
                    EmptyOutputView()
                }
            }
            .padding()
        }
        .sheet(item: $selectedOutput) { output in
            OutputDetailView(output: output)
        }
    }
}

// MARK: - 生成状态
struct GenerationStatusView: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        if project.designScheme == nil {
            VStack(spacing: 15) {
                Image(systemName: "wand.and.stars")
                    .font(.system(size: 48))
                    .foregroundColor(.accentColor)
                
                Text("准备生成设计方案")
                    .font(.headline)
                
                Text("请确保已完成以下设置：\n1. 导入规划范围\n2. 选择功能类型\n3. 调整规划指标\n4. 选择设计风格")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .multilineTextAlignment(.center)
            }
            .padding(40)
            .frame(maxWidth: .infinity)
            .background(Color.gray.opacity(0.1))
            .cornerRadius(12)
        }
    }
}

// MARK: - 输出卡片
struct OutputCard: View {
    let output: DesignOutput
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            // 缩略图
            ZStack {
                if let thumbnail = output.thumbnail {
                    Image(nsImage: thumbnail)
                        .resizable()
                        .scaledToFill()
                } else {
                    Rectangle()
                        .fill(Color.gray.opacity(0.2))
                    
                    VStack {
                        Image(systemName: output.type.icon)
                            .font(.system(size: 40))
                            .foregroundColor(.gray)
                        Text(output.type.rawValue)
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }
                }
            }
            .frame(height: 150)
            .clipped()
            .cornerRadius(8)
            
            // 信息
            VStack(alignment: .leading, spacing: 4) {
                Text(output.type.rawValue)
                    .font(.subheadline)
                    .fontWeight(.medium)
                
                Text(output.createdAt, style: .date)
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            // 操作按钮
            HStack {
                Button("查看") {
                    // 查看大图
                }
                .buttonStyle(.bordered)
                .controlSize(.small)
                
                Spacer()
                
                Button("导出") {
                    // 导出文件
                }
                .buttonStyle(.borderedProminent)
                .controlSize(.small)
            }
        }
        .padding()
        .background(Color.gray.opacity(0.1))
        .cornerRadius(12)
    }
}

// MARK: - 空状态
struct EmptyOutputView: View {
    var body: some View {
        VStack(spacing: 20) {
            Spacer()
            
            Image(systemName: "photo.stack")
                .font(.system(size: 60))
                .foregroundColor(.gray)
            
            Text("暂无设计成果")
                .font(.headline)
                .foregroundColor(.secondary)
            
            Text("点击\"生成方案\"按钮开始设计")
                .font(.subheadline)
                .foregroundColor(.gray)
            
            Spacer()
        }
        .padding(60)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

// MARK: - 详情视图
struct OutputDetailView: View {
    let output: DesignOutput
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationView {
            VStack {
                if let thumbnail = output.thumbnail {
                    Image(nsImage: thumbnail)
                        .resizable()
                        .scaledToFit()
                        .padding()
                } else {
                    Text("无法加载图片")
                        .foregroundColor(.secondary)
                }
                
                HStack(spacing: 20) {
                    Button("保存到本地") {
                        saveToLocal()
                    }
                    .buttonStyle(.borderedProminent)
                    
                    Button("复制到剪贴板") {
                        copyToClipboard()
                    }
                    .buttonStyle(.bordered)
                }
                .padding()
            }
            .navigationTitle(output.type.rawValue)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("关闭") {
                        dismiss()
                    }
                }
            }
        }
        .frame(minWidth: 600, minHeight: 500)
    }
    
    private func saveToLocal() {
        // 实现保存逻辑
    }
    
    private func copyToClipboard() {
        // 实现复制逻辑
    }
}

// MARK: - 设计方案预览
struct DesignPreview: View {
    @ObservedObject var scheme: DesignScheme
    
    var body: some View {
        VStack(spacing: 0) {
            // 顶部概念说明
            ConceptHeader(concept: scheme.concept)
                .padding()
                .background(Color(.windowBackgroundColor))
            
            Divider()
            
            // 主要预览区域
            GeometryReader { geometry in
                HStack(spacing: 0) {
                    // 左侧：功能分区列表
                    ZonesList(zones: scheme.zones)
                        .frame(width: 250)
                    
                    Divider()
                    
                    // 右侧：可视化预览
                    VisualPreview(scheme: scheme)
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                }
            }
        }
    }
}

struct ConceptHeader: View {
    let concept: DesignConcept
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                VStack(alignment: .leading, spacing: 4) {
                    Text(concept.theme)
                        .font(.title2)
                        .fontWeight(.bold)
                    
                    Text(concept.philosophy)
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                        .lineLimit(2)
                }
                
                Spacer()
                
                HStack(spacing: 15) {
                    ConceptBadge(title: "空间", content: concept.spatialStructure)
                    ConceptBadge(title: "景观", content: concept.landscapeStrategy)
                }
            }
        }
    }
}

struct ConceptBadge: View {
    let title: String
    let content: String
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(title)
                .font(.caption)
                .foregroundColor(.secondary)
            Text(content)
                .font(.caption)
                .fontWeight(.medium)
                .lineLimit(1)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(Color.accentColor.opacity(0.1))
        .cornerRadius(8)
    }
}

struct ZonesList: View {
    let zones: [FunctionalZone]
    
    var body: some View {
        List(zones) { zone in
            ZoneRow(zone: zone)
        }
        .listStyle(PlainListStyle())
    }
}

struct ZoneRow: View {
    let zone: FunctionalZone
    
    var body: some View {
        HStack(spacing: 12) {
            Circle()
                .fill(zone.color)
                .frame(width: 12, height: 12)
            
            VStack(alignment: .leading, spacing: 2) {
                Text(zone.name)
                    .font(.subheadline)
                    .fontWeight(.medium)
                Text("\(Int(zone.areaRatio * 100))% · \(Int(zone.area))㎡")
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            Spacer()
        }
        .padding(.vertical, 4)
    }
}

struct VisualPreview: View {
    let scheme: DesignScheme
    
    var body: some View {
        ZStack {
            // 背景
            Color.gray.opacity(0.05)
            
            // 简化的可视化（实际项目中使用Canvas或Metal渲染）
            VStack {
                Text("设计方案可视化预览")
                    .font(.headline)
                    .foregroundColor(.secondary)
                
                Text("功能分区: \(scheme.zones.count)个")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                
                Text("建筑数量: \(scheme.buildings.count)栋")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
            }
        }
    }
}

struct EmptyDesignView: View {
    var body: some View {
        VStack(spacing: 20) {
            Spacer()
            
            Image(systemName: "cube.transparent")
                .font(.system(size: 80))
                .foregroundColor(.gray.opacity(0.5))
            
            Text("暂无设计方案")
                .font(.title2)
                .fontWeight(.medium)
                .foregroundColor(.secondary)
            
            Text("请先导入规划范围并设置参数，然后点击\"生成方案\"")
                .font(.subheadline)
                .foregroundColor(.gray)
                .multilineTextAlignment(.center)
            
            Spacer()
        }
        .padding(60)
    }
}
