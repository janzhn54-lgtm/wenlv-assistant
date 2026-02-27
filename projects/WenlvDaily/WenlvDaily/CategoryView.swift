//
//  CategoryView.swift
//  分类浏览页面
//

import SwiftUI

struct CategoryView: View {
    @Binding var selectedCategory: NewsCategory?
    @EnvironmentObject var newsStore: NewsStore
    
    let columns = [
        GridItem(.flexible()),
        GridItem(.flexible())
    ]
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    // 分类网格
                    LazyVGrid(columns: columns, spacing: 16) {
                        ForEach(NewsCategory.allCases) { category in
                            CategoryGridItem(
                                category: category,
                                count: newsStore.news(for: category).count
                            )
                            .onTapGesture {
                                selectedCategory = category
                            }
                        }
                    }
                    .padding(.horizontal)
                    
                    // 如果选了分类，显示该分类的新闻
                    if let category = selectedCategory {
                        VStack(alignment: .leading, spacing: 12) {
                            HStack {
                                Text("\(category.rawValue)资讯")
                                    .font(.headline)
                                
                                Spacer()
                                
                                Button("查看全部") {
                                    // 可以跳转到完整列表
                                }
                                .font(.caption)
                                .foregroundColor(.orange)
                            }
                            .padding(.horizontal)
                            
                            ForEach(newsStore.news(for: category).prefix(5)) { item in
                                NavigationLink(destination: NewsDetailView(news: item)) {
                                    NewsCard(news: item)
                                }
                                .buttonStyle(PlainButtonStyle())
                                .padding(.horizontal)
                            }
                        }
                    }
                }
                .padding(.vertical)
            }
            .navigationTitle("分类浏览")
        }
    }
}

// MARK: - 分类网格项
struct CategoryGridItem: View {
    let category: NewsCategory
    let count: Int
    
    var body: some View {
        VStack(spacing: 12) {
            Text(category.icon)
                .font(.system(size: 40))
            
            Text(category.rawValue)
                .font(.headline)
                .fontWeight(.semibold)
            
            Text("\(count) 条资讯")
                .font(.caption)
                .foregroundColor(.gray)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 24)
        .background(categoryColor.opacity(0.1))
        .cornerRadius(16)
        .overlay(
            RoundedRectangle(cornerRadius: 16)
                .stroke(categoryColor.opacity(0.3), lineWidth: 1)
        )
    }
    
    private var categoryColor: Color {
        switch category {
        case .policy: return .blue
        case .market: return .green
        case .case_study: return .orange
        case .trend: return .purple
        }
    }
}

// MARK: - 收藏页面
struct FavoritesView: View {
    @EnvironmentObject var newsStore: NewsStore
    
    var body: some View {
        NavigationView {
            Group {
                if newsStore.favorites.isEmpty {
                    EmptyFavoritesView()
                } else {
                    List {
                        ForEach(newsStore.favorites) { item in
                            NavigationLink(destination: NewsDetailView(news: item)) {
                                FavoriteRow(news: item)
                            }
                        }
                        .onDelete { indexSet in
                            deleteFavorites(at: indexSet)
                        }
                    }
                    .listStyle(PlainListStyle())
                }
            }
            .navigationTitle("我的收藏")
            .toolbar {
                EditButton()
            }
        }
    }
    
    private func deleteFavorites(at offsets: IndexSet) {
        for index in offsets {
            let item = newsStore.favorites[index]
            newsStore.toggleFavorite(item)
        }
    }
}

// MARK: - 收藏行
struct FavoriteRow: View {
    let news: NewsItem
    
    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack {
                CategoryTag(category: news.category)
                Spacer()
                Text(news.source)
                    .font(.caption)
                    .foregroundColor(.gray)
            }
            
            Text(news.title)
                .font(.subheadline)
                .fontWeight(.medium)
                .lineLimit(2)
        }
        .padding(.vertical, 4)
    }
}

// MARK: - 空收藏视图
struct EmptyFavoritesView: View {
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "star.slash")
                .font(.system(size: 60))
                .foregroundColor(.gray)
            
            Text("暂无收藏")
                .font(.headline)
                .foregroundColor(.gray)
            
            Text("点击新闻卡片上的星标，收藏感兴趣的内容")
                .font(.subheadline)
                .foregroundColor(.gray)
                .multilineTextAlignment(.center)
                .padding(.horizontal)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .padding()
    }
}
