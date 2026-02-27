//
//  Models.swift
//  数据模型
//

import Foundation

// MARK: - 步骤枚举
enum PlanStep: Int, CaseIterable {
    case positioning = 0
    case business = 1
    case operation = 2
    case output = 3
    
    var title: String {
        switch self {
        case .positioning: return "项目定位"
        case .business: return "业态规划"
        case .operation: return "运营策略"
        case .output: return "生成方案"
        }
    }
    
    var icon: String {
        switch self {
        case .positioning: return "🎯"
        case .business: return "🏗️"
        case .operation: return "⚡"
        case .output: return "📄"
        }
    }
}

// MARK: - 定位数据
struct PositioningData {
    var projectName: String = ""
    var location: String = ""
    var locationType: LocationType?
    var targetGroups: [TargetGroup] = []
    var positioningType: PositioningType?
    var coreTheme: String = ""
    var competitors: String = ""
}

// MARK: - 业态数据
struct BusinessData {
    var coreAttractions: [AttractionType] = []
    var businessRatio: BusinessRatio = BusinessRatio()
    var circulation: CirculationType?
    var stayDuration: StayDuration?
    var ticketPrice: TicketPrice?
    var annualCapacity: AnnualCapacity?
}

struct BusinessRatio {
    var catering: Double = 30
    var retail: Double = 25
    var accommodation: Double = 20
    var entertainment: Double = 15
    var service: Double = 10
}

// MARK: - 运营数据
struct OperationData {
    var seasonFocus: [Season] = []
    var marketingChannels: [MarketingChannel] = [.douyin, .xiaohongshu, .wechat, .meituan]
    var communityFeatures: [CommunityFeature] = []
    var ipCollaboration: String = ""
    var differentiation: String = ""
}

// MARK: - 地域类型
enum LocationType: String, CaseIterable, Identifiable {
    case watertown = "江南水乡"
    case mountain = "山水生态"
    case cultural = "文化古迹"
    case coastal = "滨海度假"
    case rural = "田园乡村"
    case urban = "城市更新"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .watertown: return "🏘️"
        case .mountain: return "⛰️"
        case .cultural: return "🏛️"
        case .coastal: return "🏖️"
        case .rural: return "🌾"
        case .urban: return "🏙️"
        }
    }
    var description: String {
        switch self {
        case .watertown: return "古镇、水系、慢生活"
        case .mountain: return "自然、康养、户外"
        case .cultural: return "历史、人文、研学"
        case .coastal: return "海洋、休闲、度假"
        case .rural: return "农业、民俗、亲子"
        case .urban: return "工业遗产、文创园"
        }
    }
}

// MARK: - 目标客群
enum TargetGroup: String, CaseIterable, Identifiable {
    case family = "亲子家庭"
    case youth = "Z世代青年"
    case silver = "银发族"
    case business = "商务客群"
    case couple = "情侣/蜜月"
    case culture = "文化爱好者"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .family: return "👨‍👩‍👧‍👦"
        case .youth: return "🎒"
        case .silver: return "👴"
        case .business: return "💼"
        case .couple: return "💕"
        case .culture: return "📚"
        }
    }
    var description: String {
        switch self {
        case .family: return "3-12岁儿童家庭，注重安全与教育"
        case .youth: return "18-30岁，追求体验与社交分享"
        case .silver: return "55岁+，注重康养与品质"
        case .business: return "企业团建、会议、商务休闲"
        case .couple: return "浪漫体验、打卡拍照"
        case .culture: return "深度文化体验、研学"
        }
    }
}

// MARK: - 定位类型
enum PositioningType: String, CaseIterable, Identifiable {
    case ip = "文化IP型"
    case ecology = "生态康养型"
    case community = "社群运营型"
    case immersive = "沉浸体验型"
    case rural = "田园综合型"
    case night = "夜间经济型"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .ip: return "🎭"
        case .ecology: return "🌿"
        case .community: return "👥"
        case .immersive: return "🎪"
        case .rural: return "🏡"
        case .night: return "🌙"
        }
    }
    var description: String {
        switch self {
        case .ip: return "如拈花湾（禅意）、大唐不夜城（唐文化）"
        case .ecology: return "如莫干山、安吉，主打自然与康养"
        case .community: return "如阿那亚，用社群凝聚高粘性用户"
        case .immersive: return "如只有河南，戏剧+文旅深度融合"
        case .rural: return "如袁家村，民俗+美食+住宿"
        case .night: return "灯光秀、夜市、夜演、夜宿"
        }
    }
}

// MARK: - 吸引物类型
enum AttractionType: String, CaseIterable, Identifiable {
    case landmark = "地标景观"
    case performance = "演艺活动"
    case experience = "沉浸体验"
    case museum = "文化场馆"
    case nature = "自然景观"
    case night = "夜间项目"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .landmark: return "🏛️"
        case .performance: return "🎭"
        case .experience: return "🎪"
        case .museum: return "🏺"
        case .nature: return "🌲"
        case .night: return "🌙"
        }
    }
    var examples: String {
        switch self {
        case .landmark: return "白塔、摩天轮、观景塔"
        case .performance: return "实景演出、光影秀、巡游"
        case .experience: return "剧本杀、VR体验、互动装置"
        case .museum: return "博物馆、美术馆、非遗馆"
        case .nature: return "花海、湿地、森林公园"
        case .night: return "灯光秀、夜市、夜演"
        }
    }
}

// MARK: - 动线类型
enum CirculationType: String, CaseIterable, Identifiable {
    case loop = "环线式"
    case spine = "主轴式"
    case cluster = "组团式"
    case network = "网络式"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .loop: return "🔄"
        case .spine: return "📍"
        case .cluster: return "🔷"
        case .network: return "🔗"
        }
    }
    var description: String {
        switch self {
        case .loop: return "游客沿环形路线游览，适合中小型项目"
        case .spine: return "一条主街串联各节点，如古镇街道"
        case .cluster: return "多个主题组团，适合大型综合项目"
        case .network: return "多路径自由探索，适合开放式景区"
        }
    }
}

// MARK: - 停留时长
enum StayDuration: String, CaseIterable, Identifiable {
    case halfDay = "2-4小时（半日游）"
    case oneDay = "4-8小时（一日游）"
    case overnight = "1-2天（过夜游）"
    case vacation = "3天以上（度假游）"
    
    var id: String { rawValue }
}

// MARK: - 门票价格
enum TicketPrice: String, CaseIterable, Identifiable {
    case free = "免费开放"
    case low = "50元以下"
    case mid = "50-150元"
    case high = "150-300元"
    case premium = "300元以上"
    
    var id: String { rawValue }
}

// MARK: - 年容量
enum AnnualCapacity: String, CaseIterable, Identifiable {
    case small = "10万以下"
    case medium = "10-50万"
    case large = "50-100万"
    case xl = "100-300万"
    case xxl = "300万以上"
    
    var id: String { rawValue }
}

// MARK: - 季节
enum Season: String, CaseIterable, Identifiable {
    case spring = "春季"
    case summer = "夏季"
    case autumn = "秋季"
    case winter = "冬季"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .spring: return "🌸"
        case .summer: return "☀️"
        case .autumn: return "🍂"
        case .winter: return "❄️"
        }
    }
    var theme: String {
        switch self {
        case .spring: return "踏青赏花"
        case .summer: return "避暑亲水"
        case .autumn: return "丰收文化"
        case .winter: return "温泉暖冬"
        }
    }
    var activities: [String] {
        switch self {
        case .spring: return ["花海节", "风筝节", "采茶体验"]
        case .summer: return ["夜游", "水世界", "露营"]
        case .autumn: return ["丰收节", "摄影季", "美食节"]
        case .winter: return ["温泉季", "灯会", "年俗活动"]
        }
    }
}

// MARK: - 营销渠道
enum MarketingChannel: String, CaseIterable, Identifiable {
    case douyin = "抖音"
    case xiaohongshu = "小红书"
    case wechat = "微信生态"
    case meituan = "美团/携程"
    case kol = "KOL合作"
    case event = "事件营销"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .douyin: return "🎵"
        case .xiaohongshu: return "📕"
        case .wechat: return "💬"
        case .meituan: return "🎫"
        case .kol: return "⭐"
        case .event: return "🎯"
        }
    }
    var description: String {
        switch self {
        case .douyin: return "短视频种草+直播带货"
        case .xiaohongshu: return "图文种草+打卡攻略"
        case .wechat: return "公众号+小程序+社群"
        case .meituan: return "OTA平台+票务分销"
        case .kol: return "达人探店+体验官招募"
        case .event: return "造节+话题+热搜"
        }
    }
}

// MARK: - 社群功能
enum CommunityFeature: String, CaseIterable, Identifiable {
    case membership = "会员体系"
    case content = "UGC内容"
    case activity = "社群活动"
    
    var id: String { rawValue }
    var icon: String {
        switch self {
        case .membership: return "👑"
        case .content: return "📸"
        case .activity: return "🎉"
        }
    }
    var description: String {
        switch self {
        case .membership: return "积分+等级+专属权益"
        case .content: return "鼓励游客创作分享"
        case .activity: return "定期组织主题活动"
        }
    }
    var features: [String] {
        switch self {
        case .membership: return ["生日特权", "优先预约", "专属折扣"]
        case .content: return ["打卡奖励", "摄影比赛", "达人计划"]
        case .activity: return ["主题沙龙", "亲子活动", "会员日"]
        }
    }
}
