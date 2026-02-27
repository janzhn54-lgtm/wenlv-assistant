//
//  WenlvDailyApp.swift
//  文旅日报 - 每日文旅新闻精选
//

import SwiftUI

@main
struct WenlvDailyApp: App {
    @StateObject private var newsStore = NewsStore()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(newsStore)
        }
    }
}
