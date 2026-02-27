//
//  ContentView.swift
//  主界面
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        NavigationView {
            SidebarView()
                .frame(minWidth: 250, maxWidth: 300)
            
            if let project = appState.currentProject {
                MainWorkspaceView(project: project)
            } else {
                WelcomeView()
            }
        }
        .toolbar {
            ToolbarItemGroup(placement: .navigation) {
                Button(action: { appState.createNewProject() }) {
                    Label("新建", systemImage: "plus")
                }
                
                Button(action: { appState.showImportDialog() }) {
                    Label("导入", systemImage: "square.and.arrow.down")
                }
            }
            
            ToolbarItemGroup(placement: .primaryAction) {
                if appState.isGenerating {
                    ProgressView()
                        .scaleEffect(0.8)
                } else {
                    Button(action: { appState.generateDesign() }) {
                        Label("生成方案", systemImage: "wand.and.stars")
                    }
                    .disabled(appState.currentProject == nil)
                }
            }
        }
        .sheet(isPresented: $appState.showImportSheet) {
            ImportView(project: appState.currentProject ?? DesignProject())
        }
    }
}

// MARK: - 侧边栏
struct SidebarView: View {
    @State private var selectedSection: SidebarSection = .input
    
    enum SidebarSection: String, CaseIterable {
        case input = "输入"
        case parameters = "参数"
        case style = "风格"
        case output = "成果"
        
        var icon: String {
            switch self {
            case .input: return "square.and.pencil"
            case .parameters: return "slider.horizontal.3"
            case .style: return "paintpalette"
            case .output: return "photo.stack"
            }
        }
    }
    
    var body: some View {
        List {
            Section(header: Text("设计流程")) {
                ForEach(SidebarSection.allCases, id: \.self) { section in
                    NavigationLink(
                        destination: sectionView(for: section),
                        tag: section,
                        selection: $selectedSection
                    ) {
                        Label(section.rawValue, systemImage: section.icon)
                    }
                }
            }
        }
        .listStyle(SidebarListStyle())
        .frame(minWidth: 200)
    }
    
    @ViewBuilder
    func sectionView(for section: SidebarSection) -> some View {
        switch section {
        case .input:
            InputSectionView()
        case .parameters:
            ParametersSectionView()
        case .style:
            StyleSectionView()
        case .output:
            OutputSectionView()
        }
    }
}

// MARK: - 欢迎页面
struct WelcomeView: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        VStack(spacing: 30) {
            Spacer()
            
            Image(systemName: "building.2.fill")
                .font(.system(size: 80))
                .foregroundColor(.accentColor)
            
            Text("UrbanDesignAI")
                .font(.largeTitle)
                .fontWeight(.bold)
            
            Text("AI驱动的城市规划设计助手")
                .font(.title3)
                .foregroundColor(.secondary)
            
            VStack(alignment: .leading, spacing: 15) {
                FeatureRow(icon: "doc.fill", text: "支持CAD/图片/GIS多种输入")
                FeatureRow(icon: "paintpalette", text: "国内外顶尖设计团队风格")
                FeatureRow(icon: "photo.stack", text: "自动生成平面图、效果图")
                FeatureRow(icon: "brain", text: "AI学习进化，越用越聪明")
            }
            .padding(.top, 20)
            
            Spacer()
            
            HStack(spacing: 20) {
                Button("新建项目") {
                    appState.createNewProject()
                }
                .buttonStyle(.borderedProminent)
                .controlSize(.large)
                
                Button("导入文件") {
                    appState.showImportDialog()
                }
                .buttonStyle(.bordered)
                .controlSize(.large)
            }
            
            Spacer()
        }
        .frame(maxWidth: 500)
        .padding()
    }
}

struct FeatureRow: View {
    let icon: String
    let text: String
    
    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: icon)
                .foregroundColor(.accentColor)
                .frame(width: 24)
            Text(text)
                .foregroundColor(.secondary)
        }
    }
}

// MARK: - 输入页面
struct InputSectionView: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("导入规划范围")
                .font(.title2)
                .fontWeight(.bold)
            
            if let project = appState.currentProject {
                InputMethodView(project: project)
                    .padding()
                    .background(Color(.windowBackgroundColor))
                    .cornerRadius(12)
            } else {
                Text("请先新建项目")
                    .foregroundColor(.secondary)
            }
            
            Spacer()
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
    }
}

// MARK: - 参数页面
struct ParametersSectionView: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("设计参数")
                .font(.title2)
                .fontWeight(.bold)
            
            if let project = appState.currentProject {
                ParametersEditor(project: project)
                    .padding()
                    .background(Color(.windowBackgroundColor))
                    .cornerRadius(12)
            } else {
                Text("请先新建项目")
                    .foregroundColor(.secondary)
            }
            
            Spacer()
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
    }
}

// MARK: - 风格页面
struct StyleSectionView: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("设计风格与团队")
                .font(.title2)
                .fontWeight(.bold)
            
            if let project = appState.currentProject {
                StyleSelector(project: project)
                    .padding()
                    .background(Color(.windowBackgroundColor))
                    .cornerRadius(12)
            } else {
                Text("请先新建项目")
                    .foregroundColor(.secondary)
            }
            
            Spacer()
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
    }
}

// MARK: - 成果页面
struct OutputSectionView: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("设计成果")
                .font(.title2)
                .fontWeight(.bold)
            
            if let project = appState.currentProject {
                OutputGallery(project: project)
                    .padding()
                    .background(Color(.windowBackgroundColor))
                    .cornerRadius(12)
            } else {
                Text("请先新建项目")
                    .foregroundColor(.secondary)
            }
            
            Spacer()
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
    }
}

// MARK: - 主工作区
struct MainWorkspaceView: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        HStack(spacing: 0) {
            // 左侧：参数面板
            VStack(alignment: .leading, spacing: 20) {
                ProjectInfoCard(project: project)
                
                if project.inputData.boundaryFile != nil || project.inputData.boundaryImage != nil {
                    BoundaryPreview(project: project)
                }
                
                Spacer()
            }
            .frame(width: 300)
            .padding()
            .background(Color(.windowBackgroundColor))
            
            Divider()
            
            // 右侧：预览/编辑区
            VStack {
                if let scheme = project.designScheme {
                    DesignPreview(scheme: scheme)
                } else {
                    EmptyDesignView()
                }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
        }
    }
}
