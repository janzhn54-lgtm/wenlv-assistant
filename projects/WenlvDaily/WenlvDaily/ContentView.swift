//
//  ContentView.swift
//  主界面
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var newsStore: NewsStore
    @State private var selectedTab = 0
    @State private var selectedCategory: NewsCategory?
    
    var body: some View {
        TabView(selection: $selectedTab) {
            // 首页 - 每日精选
            DailyView()
                .tabItem {
                    Image(systemName: "newspaper.fill")
                    Text("今日")
                }
                .tag(0)
            
            // 分类浏览
            CategoryView(selectedCategory: $selectedCategory)
                .tabItem {
                    Image(systemName: "square.grid.2x2")
                    Text("分类")
                }
                .tag(1)
            
            // 收藏
            FavoritesView()
                .tabItem {
                    Image(systemName: "star.fill")
                    Text("收藏")
                }
                .tag(2)
            
            // 我的
            ProfileView()
                .tabItem {
                    Image(systemName: "person.fill")
                    Text("我的")
                }
                .tag(3)
        }
        .accentColor(.orange)
    }
}

// MARK: - 每日精选页面
struct DailyView: View {
    @EnvironmentObject var newsStore: NewsStore
    @State private var isRefreshing = false
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 16) {
                    // 头部横幅
                    DailyHeader(selection: newsStore.dailySelection)
                    
                    // 新闻列表
                    if newsStore.isLoading {
                        LoadingView()
                    } else {
                        LazyVStack(spacing: 12) {
                            ForEach(newsStore.news.prefix(10)) { item in
                                NavigationLink(destination: NewsDetailView(news: item)) {
                                    NewsCard(news: item)
                                }
                                .buttonStyle(PlainButtonStyle())
                            }
                        }
                        .padding(.horizontal)
                    }
                }
                .padding(.vertical)
            }
            .navigationTitle("文旅日报")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: { newsStore.fetchNews() }) {
                        Image(systemName: "arrow.clockwise")
                            .rotationEffect(.degrees(newsStore.isLoading ? 360 : 0))
                            .animation(newsStore.isLoading ? Animation.linear(duration: 1).repeatForever(autoreverses: false) : .default)
                    }
                }
            }
        }
    }
}

// MARK: - 每日精选头部
struct DailyHeader: View {
    let selection: DailySelection?
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text("每日精选")
                    .font(.title2)
                    .fontWeight(.bold)
                
                Spacer()
                
                Text(todayString)
                    .font(.caption)
                    .foregroundColor(.gray)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(Color.gray.opacity(0.1))
                    .cornerRadius(8)
            }
            
            if let selection = selection {
                Text(selection.theme)
                    .font(.headline)
                    .foregroundColor(.orange)
                
                Text(selection.editorNote)
                    .font(.subheadline)
                    .foregroundColor(.gray)
                    .lineLimit(2)
            }
        }
        .padding()
        .background(
            LinearGradient(
                gradient: Gradient(colors: [Color.orange.opacity(0.1), Color.orange.opacity(0.05)]),
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
        )
        .cornerRadius(16)
        .padding(.horizontal)
    }
    
    private var todayString: String {
        let formatter = DateFormatter()
        formatter.locale = Locale(identifier: "zh_CN")
        formatter.dateFormat = "MM月dd日 EEEE"
        return formatter.string(from: Date())
    }
}

// MARK: - 加载视图
struct LoadingView: View {
    var body: some View {
        VStack(spacing: 16) {
            ProgressView()
                .scaleEffect(1.5)
            Text("正在获取最新资讯...")
                .foregroundColor(.gray)
        }
        .frame(maxWidth: .infinity, minHeight: 200)
    }
}
