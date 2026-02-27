//
//  Models.swift
//  数据模型
//

import Foundation
import SwiftUI
import Combine

// MARK: - 设计项目
class DesignProject: ObservableObject, Identifiable {
    let id = UUID()
    @Published var name: String = "新建项目"
    @Published var createdAt: Date = Date()
    
    // 输入数据
    @Published var inputData: InputData = InputData()
    
    // 设计参数
    @Published var parameters: DesignParameters = DesignParameters()
    
    // 设计方案
    @Published var designScheme: DesignScheme?
    
    // 输出成果
    @Published var outputs: [DesignOutput] = []
}

// MARK: - 输入数据
struct InputData {
    var boundaryType: BoundaryType = .cad
    var boundaryFile: URL?
    var boundaryImage: NSImage?
    
    // 用地边界（解析后的坐标点）
    var boundaryPoints: [CGPoint] = []
    var landArea: Double = 0.0
}

enum BoundaryType: String, CaseIterable {
    case cad = "CAD文件"
    case image = "图片"
    case gis = "GIS文件"
    
    var icon: String {
        switch self {
        case .cad: return "doc.fill"
        case .image: return "photo.fill"
        case .gis: return "map.fill"
        }
    }
    
    var fileExtensions: [String] {
        switch self {
        case .cad: return ["dwg", "dxf"]
        case .image: return ["png", "jpg", "jpeg", "tiff"]
        case .gis: return ["shp", "geojson", "kml"]
        }
    }
}

// MARK: - 设计参数
struct DesignParameters {
    // 功能类型
    var functionType: FunctionType = .culturalTourism
    
    // 规划指标
    var plotRatio: Double = 1.5
    var buildingDensity: Double = 35.0
    var greenRate: Double = 30.0
    var heightLimit: Double = 24.0
    var parkingStandard: Double = 1.0  // 车位/100㎡
    
    // 设计风格
    var designStyle: DesignStyle = .chineseModern
    
    // 设计团队偏好
    var preferredTeams: [DesignTeam] = []
}

// MARK: - 功能类型
enum FunctionType: String, CaseIterable, Identifiable {
    case culturalTourism = "文旅小镇"
    case residential = "住宅社区"
    case commercial = "商业综合体"
    case office = "办公园区"
    case mixed = "混合开发"
    case industrial = "产业园区"
    
    var id: String { rawValue }
    
    var icon: String {
        switch self {
        case .culturalTourism: return "building.columns.fill"
        case .residential: return "house.fill"
        case .commercial: return "bag.fill"
        case .office: return "building.2.fill"
        case .mixed: return "square.grid.2x2.fill"
        case .industrial: return "gearshape.fill"
        }
    }
    
    var description: String {
        switch self {
        case .culturalTourism:
            return "文化体验、旅游度假、特色商业"
        case .residential:
            return "高层住宅、洋房别墅、社区配套"
        case .commercial:
            return "购物中心、街区商业、商务办公"
        case .office:
            return "写字楼、创意园区、企业总部"
        case .mixed:
            return "住宅+商业+办公综合开发"
        case .industrial:
            return "标准厂房、研发中心、物流仓储"
        }
    }
    
    var defaultPlotRatio: Double {
        switch self {
        case .culturalTourism: return 1.2
        case .residential: return 2.5
        case .commercial: return 3.0
        case .office: return 2.8
        case .mixed: return 2.2
        case .industrial: return 1.5
        }
    }
}

// MARK: - 设计风格
enum DesignStyle: String, CaseIterable, Identifiable {
    case chineseModern = "新中式"
    case minimalism = "极简现代"
    case mediterranean = "地中海"
    case europeanClassical = "欧式古典"
    case southeastAsian = "东南亚"
    case industrial = "工业风"
    case ecological = "生态自然"
    case techFuture = "科技未来"
    
    var id: String { rawValue }
    
    var icon: String {
        switch self {
        case .chineseModern: return "circle.grid.cross.fill"
        case .minimalism: return "square.fill"
        case .mediterranean: return "sun.max.fill"
        case .europeanClassical: return "building.columns.fill"
        case .southeastAsian: return "leaf.fill"
        case .industrial: return "gearshape.fill"
        case .ecological: return "tree.fill"
        case .techFuture: return "cpu.fill"
        }
    }
    
    var description: String {
        switch self {
        case .chineseModern:
            return "融合传统中式元素与现代设计手法"
        case .minimalism:
            return "简洁线条、纯粹空间、克制美学"
        case .mediterranean:
            return "浪漫色彩、拱形元素、休闲氛围"
        case .europeanClassical:
            return "对称布局、精致装饰、庄重典雅"
        case .southeastAsian:
            return "热带风情、自然材料、休闲度假"
        case .industrial:
            return "原始结构、金属材质、复古摩登"
        case .ecological:
            return "绿色环保、低碳可持续、亲自然"
        case .techFuture:
            return "智能科技、流线造型、未来感"
        }
    }
}

// MARK: - 设计团队
struct DesignTeam: Identifiable, Hashable {
    let id = UUID()
    var name: String
    var country: String
    var specialty: String
    var description: String
    var corePhilosophy: String
    var representativeWorks: [String]
    var isSelected: Bool = false
    
    static let allTeams: [DesignTeam] = [
        // 国内团队
        DesignTeam(
            name: "MAD建筑事务所",
            country: "中国",
            specialty: "文旅、公共建筑",
            description: "马岩松创立，以山水城市理念著称",
            corePhilosophy: "山水城市，建筑与自然和谐共生",
            representativeWorks: ["哈尔滨大剧院", "朝阳公园广场", "衢州体育公园"]
        ),
        DesignTeam(
            name: "GOA大象设计",
            country: "中国",
            specialty: "小镇、酒店、高端住宅",
            description: "注重场所精神与文化传承",
            corePhilosophy: "和而不同，营造有温度的场所",
            representativeWorks: ["乌镇雅园", "桃李春风", "良渚文化村"]
        ),
        DesignTeam(
            name: "蓝城集团",
            country: "中国",
            specialty: "小镇开发、乡村振兴",
            description: "宋卫平创立，理想小镇引领者",
            corePhilosophy: "比城市更温暖，比乡村更文明",
            representativeWorks: ["桃李春风", "越剧小镇", "天使小镇"]
        ),
        DesignTeam(
            name: "万科设计",
            country: "中国",
            specialty: "住宅、社区营造",
            description: "深耕社区设计，注重人文关怀",
            corePhilosophy: "建筑赞美生命，营造美好生活",
            representativeWorks: ["良渚文化村", "万科第五园", "深业上城"]
        ),
        
        // 国际团队
        DesignTeam(
            name: "BIG建筑事务所",
            country: "丹麦",
            specialty: "创新建筑、可持续设计",
            description: "Bjarke Ingels Group，以创新形态著称",
            corePhilosophy: "Yes is More，实用主义乌托邦",
            representativeWorks: ["8 House", "VIA 57 West", "Copenhill"]
        ),
        DesignTeam(
            name: "Sasaki",
            country: "美国",
            specialty: "城市规划、景观设计",
            description: "全球顶尖城市规划设计公司",
            corePhilosophy: "设计源于对场所的深刻理解",
            representativeWorks: ["旧金山滨水区", "北京奥林匹克公园", "深圳湾"]
        ),
        DesignTeam(
            name: "AECOM",
            country: "美国",
            specialty: "基础设施、城市设计",
            description: "全球顶尖基础设施设计公司",
            corePhilosophy: "交付更好的世界",
            representativeWorks: ["伦敦奥运公园", "上海虹桥商务区", "迪拜地铁"]
        ),
        DesignTeam(
            name: "SOM",
            country: "美国",
            specialty: "超高层、综合体",
            description: "Skidmore, Owings & Merrill",
            corePhilosophy: "整体设计，技术与艺术的融合",
            representativeWorks: ["哈利法塔", "世贸中心一号楼", "上海金茂大厦"]
        ),
        DesignTeam(
            name: "Zaha Hadid Architects",
            country: "英国",
            specialty: "参数化设计、流线造型",
            description: "扎哈·哈迪德建筑事务所",
            corePhilosophy: "建筑作为动态的力量场",
            representativeWorks: ["广州大剧院", "北京大兴机场", "望京SOHO"]
        ),
        DesignTeam(
            name: "Kengo Kuma",
            country: "日本",
            specialty: "自然材料、场所精神",
            description: "隈研吾建筑都市设计事务所",
            corePhilosophy: "让建筑消失，与自然对话",
            representativeWorks: ["长城脚下的公社", "东京奥运会场馆", "浅草文化观光中心"]
        ),
        DesignTeam(
            name: "WOHA",
            country: "新加坡",
            specialty: "热带建筑、垂直绿化",
            description: "新加坡顶级建筑事务所",
            corePhilosophy: "花园中的城市，垂直村落",
            representativeWorks: ["皮克林宾乐雅酒店", "新加坡学校", "Oasia酒店"]
        ),
        DesignTeam(
            name: "Snøhetta",
            country: "挪威",
            specialty: "景观建筑、文化建筑",
            description: "斯诺赫塔建筑事务所",
            corePhilosophy: "社会参与，环境共生",
            representativeWorks: [" Oslo歌剧院", "9/11纪念博物馆", "上海大歌剧院"]
        )
    ]
}

// MARK: - 功能分区
struct FunctionalZone: Identifiable {
    let id = UUID()
    var name: String
    var areaRatio: Double
    var area: Double
    var description: String
    var color: Color
}

// MARK: - 设计方案
class DesignScheme: ObservableObject {
    @Published var concept: DesignConcept = DesignConcept()
    @Published var zones: [FunctionalZone] = []
    @Published var buildings: [Building] = []
    @Published var landscape: LandscapeDesign = LandscapeDesign()
}

struct DesignConcept {
    var theme: String = ""
    var philosophy: String = ""
    var spatialStructure: String = ""
    var functionalLayout: String = ""
    var landscapeStrategy: String = ""
    var buildingForm: String = ""
    var designLogic: String = ""
}

struct Building {
    var id = UUID()
    var name: String
    var position: CGPoint
    var size: CGSize
    var height: Double
    var floors: Int
    var function: String
}

struct LandscapeDesign {
    var greenSpaces: [GreenSpace] = []
    var waterFeatures: [WaterFeature] = []
    var pedestrianPaths: [Path] = []
}

struct GreenSpace {
    var id = UUID()
    var name: String
    var area: Double
    var type: String
}

struct WaterFeature {
    var id = UUID()
    var name: String
    var type: String  // 湖泊/溪流/喷泉
}

struct Path {
    var id = UUID()
    var name: String
    var width: Double
    var points: [CGPoint]
}

// MARK: - 设计输出
struct DesignOutput: Identifiable {
    let id = UUID()
    var type: OutputType
    var fileURL: URL?
    var thumbnail: NSImage?
    var createdAt: Date
}

enum OutputType: String, CaseIterable {
    case cadPlan = "CAD平面图"
    case coloredPlan = "彩色平面图"
    case birdEye = "鸟瞰图"
    case humanView = "人视图"
    case analysis = "分析图"
    case document = "设计文档"
    
    var icon: String {
        switch self {
        case .cadPlan: return "doc.fill"
        case .coloredPlan: return "paintbrush.fill"
        case .birdEye: return "airplane"
        case .humanView: return "eye.fill"
        case .analysis: return "chart.bar.fill"
        case .document: return "text.document.fill"
        }
    }
}
