//
//  NewsStore.swift
//  数据管理
//

import Foundation
import Combine

class NewsStore: ObservableObject {
    @Published var news: [NewsItem] = []
    @Published var favorites: [NewsItem] = []
    @Published var dailySelection: DailySelection?
    @Published var isLoading = false
    @Published var lastUpdate: Date?
    
    private let userDefaults = UserDefaults.standard
    private let newsKey = "savedNews"
    private let favoritesKey = "favoriteNews"
    
    init() {
        loadSavedNews()
        fetchNews()
    }
    
    // MARK: - 获取新闻
    func fetchNews() {
        isLoading = true
        
        // 模拟网络请求，实际使用RSS或API
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) { [weak self] in
            self?.news = Self.mockNews()
            self?.dailySelection = Self.mockDailySelection()
            self?.isLoading = false
            self?.lastUpdate = Date()
            self?.saveNews()
        }
    }
    
    // MARK: - 收藏管理
    func toggleFavorite(_ item: NewsItem) {
        if let index = news.firstIndex(where: { $0.id == item.id }) {
            news[index].isFavorite.toggle()
            updateFavorites()
            saveNews()
        }
    }
    
    func updateFavorites() {
        favorites = news.filter { $0.isFavorite }
    }
    
    // MARK: - 标记已读
    func markAsRead(_ item: NewsItem) {
        if let index = news.firstIndex(where: { $0.id == item.id }) {
            news[index].isRead = true
            saveNews()
        }
    }
    
    // MARK: - 本地存储
    private func saveNews() {
        if let encoded = try? JSONEncoder().encode(news) {
            userDefaults.set(encoded, forKey: newsKey)
        }
    }
    
    private func loadSavedNews() {
        if let data = userDefaults.data(forKey: newsKey),
           let decoded = try? JSONDecoder().decode([NewsItem].self, from: data) {
            news = decoded
            updateFavorites()
        }
    }
    
    // MARK: - 按分类筛选
    func news(for category: NewsCategory?) -> [NewsItem] {
        guard let category = category else { return news }
        return news.filter { $0.category == category }
    }
    
    // MARK: - 统计数据
    var stats: (total: Int, read: Int, favorites: Int) {
        (news.count, news.filter { $0.isRead }.count, favorites.count)
    }
}

// MARK: - 模拟数据
extension NewsStore {
    static func mockNews() -> [NewsItem] {
        [
            NewsItem(
                title: "文旅部发布2025年乡村旅游重点村名单",
                summary: "文化和旅游部公布新一批全国乡村旅游重点村名单，共300个村庄入选，浙江绍兴多地上榜...",
                category: .policy,
                source: "文旅部官网",
                link: "https://example.com/1"
            ),
            NewsItem(
                title: "拈花湾文旅集团Q4营收同比增长35%",
                summary: "禅意小镇模式持续火爆，夜游经济成为新增长点，沉浸式体验项目贡献超40%收入...",
                category: .market,
                source: "证券时报",
                link: "https://example.com/2"
            ),
            NewsItem(
                title: "阿那亚社群运营模式深度解析",
                summary: "从海边社区到文化地标，阿那亚用十年时间打造了中国最成功的高端文旅社群...",
                category: .case_study,
                source: "文旅研究院",
                link: "https://example.com/3"
            ),
            NewsItem(
                title: "2025文旅十大趋势预测",
                summary: "Z世代成消费主力、数字文旅加速、沉浸式体验升级、乡村振兴深度融合...",
                category: .trend,
                source: "中国旅游报",
                link: "https://example.com/4"
            ),
            NewsItem(
                title: "绍兴古城保护条例正式实施",
                summary: "条例明确了古城保护范围、保护措施和开发限制，为绍兴文旅发展提供法治保障...",
                category: .policy,
                source: "绍兴日报",
                link: "https://example.com/5"
            ),
            NewsItem(
                title: "迪士尼新园区落户中国某二线城市",
                summary: "华特迪士尼公司宣布将在中西部某省会城市投资建设全新主题公园，预计2028年开园...",
                category: .market,
                source: "财经网",
                link: "https://example.com/6"
            ),
            NewsItem(
                title: "袁家村模式：从关中民俗到全国复制",
                summary: "以美食为切入点的乡村旅游模式如何成功走向全国，袁家村给出了教科书级别的答案...",
                category: .case_study,
                source: "乡村旅游杂志",
                link: "https://example.com/7"
            ),
            NewsItem(
                title: "AI导游正在取代传统导游吗？",
                summary: "随着大模型技术成熟，越来越多的景区开始试水AI智能导览，传统导游面临转型挑战...",
                category: .trend,
                source: "科技日报",
                link: "https://example.com/8"
            )
        ]
    }
    
    static func mockDailySelection() -> DailySelection {
        DailySelection(
            date: Date(),
            news: Array(mockNews().prefix(5)),
            theme: "政策红利与市场机遇并存",
            editorNote: "本期精选重点关注最新政策动向和头部企业财报，乡村旅游和沉浸式体验持续升温。"
        )
    }
}
