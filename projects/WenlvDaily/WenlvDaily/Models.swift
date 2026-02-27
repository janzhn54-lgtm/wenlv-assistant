//
//  Models.swift
//  数据模型
//

import Foundation

// MARK: - 新闻分类
enum NewsCategory: String, CaseIterable, Identifiable {
    case policy = "政策"
    case market = "市场"
    case case_study = "案例"
    case trend = "趋势"
    
    var id: String { rawValue }
    
    var icon: String {
        switch self {
        case .policy: return "📋"
        case .market: return "📈"
        case .case_study: return "💡"
        case .trend: return "🔮"
        }
    }
    
    var color: String {
        switch self {
        case .policy: return "blue"
        case .market: return "green"
        case .case_study: return "orange"
        case .trend: return "purple"
        }
    }
}

// MARK: - 新闻模型
struct NewsItem: Identifiable, Codable {
    let id: String
    let title: String
    let summary: String
    let category: NewsCategory
    let source: String
    let publishDate: Date
    let imageURL: String?
    let link: String
    var isRead: Bool
    var isFavorite: Bool
    
    init(id: String = UUID().uuidString,
         title: String,
         summary: String,
         category: NewsCategory,
         source: String,
         publishDate: Date = Date(),
         imageURL: String? = nil,
         link: String,
         isRead: Bool = false,
         isFavorite: Bool = false) {
        self.id = id
        self.title = title
        self.summary = summary
        self.category = category
        self.source = source
        self.publishDate = publishDate
        self.imageURL = imageURL
        self.link = link
        self.isRead = isRead
        self.isFavorite = isFavorite
    }
}

// MARK: - 每日精选
struct DailySelection: Identifiable {
    let id = UUID()
    let date: Date
    let news: [NewsItem]
    let theme: String
    let editorNote: String
}

// MARK: - 用户设置
struct UserSettings: Codable {
    var isDarkMode: Bool
    var notificationEnabled: Bool
    var dailyPushTime: Date
    var preferredCategories: [NewsCategory]
    
    static let `default` = UserSettings(
        isDarkMode: false,
        notificationEnabled: true,
        dailyPushTime: Calendar.current.date(from: DateComponents(hour: 8, minute: 0))!,
        preferredCategories: NewsCategory.allCases
    )
}
