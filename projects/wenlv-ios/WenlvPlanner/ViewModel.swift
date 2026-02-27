//
//  ViewModel.swift
//  视图模型
//

import Foundation
import Combine

class PlanViewModel: ObservableObject {
    @Published var currentStep: PlanStep = .positioning
    
    // 各步骤数据
    @Published var positioningData = PositioningData()
    @Published var businessData = BusinessData()
    @Published var operationData = OperationData()
    
    // 生成状态
    @Published var isGenerating = false
    @Published var generatedPlan: PlanResult?
    
    // MARK: - 导航方法
    func goToNextStep() {
        if let next = PlanStep(rawValue: currentStep.rawValue + 1) {
            currentStep = next
        }
    }
    
    func goToPreviousStep() {
        if let prev = PlanStep(rawValue: currentStep.rawValue - 1) {
            currentStep = prev
        }
    }
    
    func goToStep(_ step: PlanStep) {
        currentStep = step
    }
    
    // MARK: - 生成方案
    func generatePlan() {
        isGenerating = true
        
        // 模拟生成过程
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) { [weak self] in
            self?.generatedPlan = self?.createPlanResult()
            self?.isGenerating = false
        }
    }
    
    private func createPlanResult() -> PlanResult {
        return PlanResult(
            title: "\(positioningData.projectName.isEmpty ? "文旅项目" : positioningData.projectName) 策划方案",
            summary: generateSummary(),
            positioning: positioningData,
            business: businessData,
            operation: operationData
        )
    }
    
    private func generateSummary() -> String {
        let location = positioningData.location.isEmpty ? "待定" : positioningData.location
        let locationType = positioningData.locationType?.rawValue ?? "地域"
        let theme = positioningData.coreTheme.isEmpty ? "文化" : positioningData.coreTheme
        let positioning = positioningData.positioningType?.rawValue ?? "特色"
        
        return "本项目位于\(location)，依托\(locationType)资源，以\"\(theme)\"为核心主题，打造\(positioning)文旅目的地。"
    }
    
    // MARK: - 导出功能
    func exportAsMarkdown() -> String {
        guard let plan = generatedPlan else { return "" }
        return plan.toMarkdown()
    }
    
    func exportAsText() -> String {
        guard let plan = generatedPlan else { return "" }
        return plan.toText()
    }
    
    // MARK: - 重置
    func reset() {
        positioningData = PositioningData()
        businessData = BusinessData()
        operationData = OperationData()
        generatedPlan = nil
        currentStep = .positioning
    }
}

// MARK: - 方案结果
struct PlanResult {
    let title: String
    let summary: String
    let positioning: PositioningData
    let business: BusinessData
    let operation: OperationData
    
    func toMarkdown() -> String {
        return """
        # \(title)
        
        ## 项目概述
        
        \(summary)
        
        ---
        
        ## 一、项目定位
        
        ### 1.1 地理位置
        - **项目位置**: \(positioning.location.isEmpty ? "待定" : positioning.location)
        - **资源类型**: \(positioning.locationType?.rawValue ?? "待定")
        
        ### 1.2 目标客群
        \(positioning.targetGroups.map(\\.rawValue).joined(separator: "、").isEmpty ? "待定" : positioning.targetGroups.map(\\.rawValue).joined(separator: "、"))
        
        ### 1.3 项目定位
        - **定位类型**: \(positioning.positioningType?.rawValue ?? "待定")
        - **核心主题**: \(positioning.coreTheme.isEmpty ? "待定" : positioning.coreTheme)
        
        ### 1.4 竞品分析
        \(positioning.competitors.isEmpty ? "待定" : positioning.competitors)
        
        ---
        
        ## 二、业态规划
        
        ### 2.1 核心吸引物
        \(business.coreAttractions.map(\\.rawValue).joined(separator: "、").isEmpty ? "待定" : business.coreAttractions.map(\\.rawValue).joined(separator: "、"))
        
        ### 2.2 业态配比
        - 餐饮: \(Int(business.businessRatio.catering))%
        - 零售: \(Int(business.businessRatio.retail))%
        - 住宿: \(Int(business.businessRatio.accommodation))%
        - 娱乐: \(Int(business.businessRatio.entertainment))%
        - 服务: \(Int(business.businessRatio.service))%
        
        ### 2.3 动线设计
        \(business.circulation?.rawValue ?? "待定")
        
        ### 2.4 运营指标
        - 停留时长: \(business.stayDuration?.rawValue ?? "待定")
        - 门票价格: \(business.ticketPrice?.rawValue ?? "待定")
        - 年容量: \(business.annualCapacity?.rawValue ?? "待定")
        
        ---
        
        ## 三、运营策略
        
        ### 3.1 四季运营
        重点发力: \(operation.seasonFocus.map(\\.rawValue).joined(separator: "、").isEmpty ? "全年" : operation.seasonFocus.map(\\.rawValue).joined(separator: "、"))
        
        ### 3.2 营销渠道
        \(operation.marketingChannels.map(\\.rawValue).joined(separator: "、"))
        
        ### 3.3 社群运营
        \(operation.communityFeatures.map(\\.rawValue).joined(separator: "、").isEmpty ? "待定" : operation.communityFeatures.map(\\.rawValue).joined(separator: "、"))
        
        ### 3.4 IP 合作
        \(operation.ipCollaboration.isEmpty ? "待定" : operation.ipCollaboration)
        
        ### 3.5 差异化优势
        \(operation.differentiation.isEmpty ? "待定" : operation.differentiation)
        
        ---
        
        *本方案由文旅策划生成器自动生成*
        """
    }
    
    func toText() -> String {
        return """
        \(title)
        
        项目概述：\(summary)
        
        一、项目定位
        地理位置：\(positioning.location.isEmpty ? "待定" : positioning.location)
        资源类型：\(positioning.locationType?.rawValue ?? "待定")
        目标客群：\(positioning.targetGroups.map(\\.rawValue).joined(separator: "、").isEmpty ? "待定" : positioning.targetGroups.map(\\.rawValue).joined(separator: "、"))
        项目定位：\(positioning.positioningType?.rawValue ?? "待定")
        核心主题：\(positioning.coreTheme.isEmpty ? "待定" : positioning.coreTheme)
        
        二、业态规划
        核心吸引物：\(business.coreAttractions.map(\\.rawValue).joined(separator: "、").isEmpty ? "待定" : business.coreAttractions.map(\\.rawValue).joined(separator: "、"))
        业态配比：餐饮\(Int(business.businessRatio.catering))% / 零售\(Int(business.businessRatio.retail))% / 住宿\(Int(business.businessRatio.accommodation))% / 娱乐\(Int(business.businessRatio.entertainment))% / 服务\(Int(business.businessRatio.service))%
        动线设计：\(business.circulation?.rawValue ?? "待定")
        
        三、运营策略
        四季运营：\(operation.seasonFocus.map(\\.rawValue).joined(separator: "、").isEmpty ? "全年" : operation.seasonFocus.map(\\.rawValue).joined(separator: "、"))
        营销渠道：\(operation.marketingChannels.map(\\.rawValue).joined(separator: "、"))
        社群运营：\(operation.communityFeatures.map(\\.rawValue).joined(separator: "、").isEmpty ? "待定" : operation.communityFeatures.map(\\.rawValue).joined(separator: "、"))
        
        本方案由文旅策划生成器自动生成
        """
    }
}
