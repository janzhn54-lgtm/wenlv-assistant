//
//  UrbanDesignAIApp.swift
//  AI城市规划设计助手 - Mac原生App
//

import SwiftUI

@main
struct UrbanDesignAIApp: App {
    @StateObject private var appState = AppState()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(appState)
                .frame(minWidth: 1200, minHeight: 800)
        }
        .windowStyle(.titleBar)
        .commands {
            CommandMenu("设计") {
                Button("新建项目") {
                    appState.createNewProject()
                }
                .keyboardShortcut("n", modifiers: .command)
                
                Button("导入文件") {
                    appState.showImportDialog()
                }
                .keyboardShortcut("i", modifiers: .command)
                
                Divider()
                
                Button("生成方案") {
                    appState.generateDesign()
                }
                .keyboardShortcut("g", modifiers: .command)
            }
        }
    }
}

class AppState: ObservableObject {
    @Published var currentProject: DesignProject?
    @Published var isGenerating = false
    @Published var showImportSheet = false
    
    func createNewProject() {
        currentProject = DesignProject()
    }
    
    func showImportDialog() {
        showImportSheet = true
    }
    
    func generateDesign() {
        guard currentProject != nil else { return }
        isGenerating = true
        // 实际项目中这里调用AI生成
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            self.isGenerating = false
        }
    }
}
