//
//  ContentView.swift
//  主入口视图
//

import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = PlanViewModel()
    
    var body: some View {
        NavigationView {
            VStack(spacing: 0) {
                // 顶部标题
                HeaderView()
                
                // 步骤指示器
                StepIndicator(currentStep: viewModel.currentStep)
                    .padding(.vertical, 10)
                
                // 主内容区
                TabView(selection: $viewModel.currentStep) {
                    PositioningView(viewModel: viewModel)
                        .tag(PlanStep.positioning)
                    
                    BusinessView(viewModel: viewModel)
                        .tag(PlanStep.business)
                    
                    OperationView(viewModel: viewModel)
                        .tag(PlanStep.operation)
                    
                    OutputView(viewModel: viewModel)
                        .tag(PlanStep.output)
                }
                .tabViewStyle(PageTabViewStyle(indexDisplayMode: .never))
                .animation(.easeInOut, value: viewModel.currentStep)
            }
            .navigationBarHidden(true)
        }
    }
}

// MARK: - 头部视图
struct HeaderView: View {
    var body: some View {
        HStack {
            Image(systemName: "building.columns.fill")
                .font(.title)
                .foregroundColor(.orange)
            
            VStack(alignment: .leading, spacing: 2) {
                Text("文旅策划生成器")
                    .font(.headline)
                    .fontWeight(.bold)
                
                Text("专业文旅项目策划方案一键生成")
                    .font(.caption)
                    .foregroundColor(.gray)
            }
            
            Spacer()
        }
        .padding()
        .background(Color.orange.opacity(0.1))
    }
}

// MARK: - 步骤指示器
struct StepIndicator: View {
    let currentStep: PlanStep
    
    var body: some View {
        HStack(spacing: 16) {
            ForEach(PlanStep.allCases, id: \.self) { step in
                StepItem(
                    step: step,
                    isActive: currentStep == step,
                    isCompleted: step.rawValue < currentStep.rawValue
                )
            }
        }
        .padding(.horizontal)
    }
}

struct StepItem: View {
    let step: PlanStep
    let isActive: Bool
    let isCompleted: Bool
    
    var body: some View {
        HStack(spacing: 4) {
            Text(step.icon)
            Text(step.title)
                .font(.caption)
                .fontWeight(isActive ? .bold : .regular)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
        .background(
            isActive ? Color.orange : (isCompleted ? Color.green.opacity(0.2) : Color.gray.opacity(0.1))
        )
        .foregroundColor(isActive ? .white : (isCompleted ? .green : .gray))
        .cornerRadius(20)
    }
}
