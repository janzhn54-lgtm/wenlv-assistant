//
//  NewsCard.swift
//  新闻卡片组件
//

import SwiftUI

struct NewsCard: View {
    let news: NewsItem
    @EnvironmentObject var newsStore: NewsStore
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            // 分类标签和来源
            HStack {
                CategoryTag(category: news.category)
                
                Spacer()
                
                Text(news.source)
                    .font(.caption)
                    .foregroundColor(.gray)
                
                if news.isFavorite {
                    Image(systemName: "star.fill")
                        .foregroundColor(.yellow)
                        .font(.caption)
                }
            }
            
            // 标题
            Text(news.title)
                .font(.headline)
                .fontWeight(.semibold)
                .lineLimit(2)
                .foregroundColor(news.isRead ? .gray : .primary)
            
            // 摘要
            Text(news.summary)
                .font(.subheadline)
                .foregroundColor(.gray)
                .lineLimit(2)
            
            // 底部信息
            HStack {
                Text(timeAgoString(from: news.publishDate))
                    .font(.caption)
                    .foregroundColor(.gray)
                
                Spacer()
                
                Button(action: {
                    newsStore.toggleFavorite(news)
                }) {
                    Image(systemName: news.isFavorite ? "star.fill" : "star")
                        .foregroundColor(news.isFavorite ? .yellow : .gray)
                }
            }
        }
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(12)
        .shadow(color: .black.opacity(0.05), radius: 5, x: 0, y: 2)
        .overlay(
            RoundedRectangle(cornerRadius: 12)
                .stroke(news.isRead ? Color.clear : Color.orange.opacity(0.3), lineWidth: news.isRead ? 0 : 1)
        )
    }
    
    private func timeAgoString(from date: Date) -> String {
        let formatter = RelativeDateTimeFormatter()
        formatter.locale = Locale(identifier: "zh_CN")
        return formatter.localizedString(for: date, relativeTo: Date())
    }
}

// MARK: - 分类标签
struct CategoryTag: View {
    let category: NewsCategory
    
    var body: some View {
        HStack(spacing: 4) {
            Text(category.icon)
            Text(category.rawValue)
        }
        .font(.caption)
        .fontWeight(.medium)
        .foregroundColor(tagColor)
        .padding(.horizontal, 8)
        .padding(.vertical, 4)
        .background(tagColor.opacity(0.15))
        .cornerRadius(6)
    }
    
    private var tagColor: Color {
        switch category {
        case .policy: return .blue
        case .market: return .green
        case .case_study: return .orange
        case .trend: return .purple
        }
    }
}

// MARK: - 新闻详情页
struct NewsDetailView: View {
    let news: NewsItem
    @EnvironmentObject var newsStore: NewsStore
    @Environment(\.presentationMode) var presentationMode
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                // 分类和时间
                HStack {
                    CategoryTag(category: news.category)
                    Spacer()
                    Text(news.source)
                        .font(.subheadline)
                        .foregroundColor(.gray)
                }
                
                // 标题
                Text(news.title)
                    .font(.title)
                    .fontWeight(.bold)
                
                // 发布时间
                Text(formatDate(news.publishDate))
                    .font(.caption)
                    .foregroundColor(.gray)
                
                Divider()
                
                // 正文（这里模拟完整内容）
                Text(news.summary + "\n\n" + mockFullContent())
                    .font(.body)
                    .lineSpacing(6)
                
                Spacer()
                
                // 底部操作栏
                HStack(spacing: 20) {
                    Button(action: {
                        newsStore.toggleFavorite(news)
                    }) {
                        HStack {
                            Image(systemName: news.isFavorite ? "star.fill" : "star")
                            Text(news.isFavorite ? "已收藏" : "收藏")
                        }
                        .foregroundColor(news.isFavorite ? .yellow : .orange)
                        .padding(.horizontal, 16)
                        .padding(.vertical, 10)
                        .background(Color.orange.opacity(0.1))
                        .cornerRadius(8)
                    }
                    
                    Button(action: shareNews) {
                        HStack {
                            Image(systemName: "square.and.arrow.up")
                            Text("分享")
                        }
                        .foregroundColor(.blue)
                        .padding(.horizontal, 16)
                        .padding(.vertical, 10)
                        .background(Color.blue.opacity(0.1))
                        .cornerRadius(8)
                    }
                    
                    Spacer()
                }
            }
            .padding()
        }
        .navigationBarTitleDisplayMode(.inline)
        .onAppear {
            newsStore.markAsRead(news)
        }
    }
    
    private func formatDate(_ date: Date) -> String {
        let formatter = DateFormatter()
        formatter.locale = Locale(identifier: "zh_CN")
        formatter.dateFormat = "yyyy年MM月dd日 HH:mm"
        return formatter.string(from: date)
    }
    
    private func mockFullContent() -> String {
        """
        据相关负责人透露，这一举措将为文旅产业带来新的发展机遇。专家表示，随着消费升级和旅游需求的多样化，文旅融合已成为行业发展的重要趋势。

        业内人士分析认为，这一政策的出台将进一步推动乡村旅游提质增效，助力乡村振兴战略实施。同时，也将为相关企业提供更多的发展空间和市场机遇。

        值得注意的是，此次入选的村庄在保持传统风貌的同时，也注重创新发展模式的探索。通过引入新业态、新模式，实现了文化传承与经济发展的良性互动。

        未来，随着相关配套措施的逐步完善，预计将有更多的优质文旅项目涌现，为游客提供更加丰富多样的旅游体验。
        """
    }
    
    private func shareNews() {
        // 实际应用中使用 ShareSheet
        print("分享新闻: \(news.title)")
    }
}
