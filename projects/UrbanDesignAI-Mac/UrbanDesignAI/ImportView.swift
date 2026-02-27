//
//  ImportView.swift
//  导入文件对话框
//

import SwiftUI

struct ImportView: View {
    @ObservedObject var project: DesignProject
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                // 说明文字
                VStack(spacing: 10) {
                    Image(systemName: "square.and.arrow.down")
                        .font(.system(size: 48))
                        .foregroundColor(.accentColor)
                    
                    Text("导入规划范围文件")
                        .font(.title2)
                        .fontWeight(.bold)
                    
                    Text("支持 CAD图纸、图片、GIS数据")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                }
                .padding(.top, 20)
                
                // 导入方式选择
                VStack(spacing: 15) {
                    ImportMethodButton(
                        icon: "doc.fill",
                        title: "导入CAD文件",
                        subtitle: "支持 .dwg, .dxf 格式",
                        action: { importCAD() }
                    )
                    
                    ImportMethodButton(
                        icon: "photo.fill",
                        title: "导入图片",
                        subtitle: "支持 .png, .jpg, .tiff 格式",
                        action: { importImage() }
                    )
                    
                    ImportMethodButton(
                        icon: "map.fill",
                        title: "导入GIS数据",
                        subtitle: "支持 .shp, .geojson, .kml 格式",
                        action: { importGIS() }
                    )
                }
                .padding(.horizontal)
                
                Spacer()
                
                // 取消按钮
                Button("取消") {
                    dismiss()
                }
                .buttonStyle(.bordered)
                .controlSize(.large)
                .padding(.bottom, 20)
            }
            .frame(width: 400, height: 500)
            .navigationTitle("导入文件")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("关闭") {
                        dismiss()
                    }
                }
            }
        }
    }
    
    private func importCAD() {
        // 打开CAD文件选择器
        let panel = NSOpenPanel()
        panel.allowedContentTypes = [.init(filenameExtension: "dwg")!, .init(filenameExtension: "dxf")!]
        panel.allowsMultipleSelection = false
        panel.canChooseDirectories = false
        
        if panel.runModal() == .OK, let url = panel.url {
            project.inputData.boundaryFile = url
            project.inputData.boundaryType = .cad
            // 解析CAD文件
            parseCADFile(url: url)
            dismiss()
        }
    }
    
    private func importImage() {
        let panel = NSOpenPanel()
        panel.allowedContentTypes = [.png, .jpeg, .tiff]
        panel.allowsMultipleSelection = false
        
        if panel.runModal() == .OK, let url = panel.url {
            project.inputData.boundaryFile = url
            project.inputData.boundaryType = .image
            if let image = NSImage(contentsOf: url) {
                project.inputData.boundaryImage = image
                parseImage(image: image)
            }
            dismiss()
        }
    }
    
    private func importGIS() {
        let panel = NSOpenPanel()
        panel.allowedContentTypes = [.init(filenameExtension: "shp")!, .init(filenameExtension: "geojson")!]
        panel.allowsMultipleSelection = false
        
        if panel.runModal() == .OK, let url = panel.url {
            project.inputData.boundaryFile = url
            project.inputData.boundaryType = .gis
            parseGISFile(url: url)
            dismiss()
        }
    }
    
    private func parseCADFile(url: URL) {
        // 实际项目中调用CAD解析库
        // 简化版：设置示例数据
        project.inputData.boundaryPoints = [
            CGPoint(x: 0, y: 0),
            CGPoint(x: 100, y: 0),
            CGPoint(x: 120, y: 80),
            CGPoint(x: 80, y: 100),
            CGPoint(x: 20, y: 90)
        ]
        project.inputData.landArea = 9900.0
    }
    
    private func parseImage(image: NSImage) {
        let size = image.size
        project.inputData.boundaryPoints = [
            CGPoint(x: 0, y: 0),
            CGPoint(x: size.width, y: 0),
            CGPoint(x: size.width, y: size.height),
            CGPoint(x: 0, y: size.height)
        ]
        project.inputData.landArea = Double(size.width * size.height) / 10000.0
    }
    
    private func parseGISFile(url: URL) {
        // 实际项目中调用GIS解析库
        parseCADFile(url: url)
    }
}

struct ImportMethodButton: View {
    let icon: String
    let title: String
    let subtitle: String
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            HStack(spacing: 15) {
                Image(systemName: icon)
                    .font(.system(size: 32))
                    .foregroundColor(.accentColor)
                    .frame(width: 50)
                
                VStack(alignment: .leading, spacing: 4) {
                    Text(title)
                        .font(.headline)
                        .foregroundColor(.primary)
                    
                    Text(subtitle)
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                
                Spacer()
                
                Image(systemName: "chevron.right")
                    .foregroundColor(.gray)
            }
            .padding()
            .background(Color.gray.opacity(0.1))
            .cornerRadius(12)
        }
        .buttonStyle(PlainButtonStyle())
    }
}
