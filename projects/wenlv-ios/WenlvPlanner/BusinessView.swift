//
//  BusinessView.swift
//  业态规划页面
//

import SwiftUI

struct BusinessView: View {
    @ObservedObject var viewModel: PlanViewModel
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                // 标题
                VStack(alignment: .leading, spacing: 4) {
                    Text("🏗️ 业态规划")
                        .font(.title2)
                        .fontWeight(.bold)
                    Text("设计核心吸引物、业态配比和游客动线")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                }
                
                // 核心吸引物
                SelectionSection(title: "核心吸引物（可多选）") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 150))], spacing: 12) {
                        ForEach(AttractionType.allCases) { type in
                            MultiSelectableCard(
                                icon: type.icon,
                                title: type.rawValue,
                                subtitle: type.examples,
                                isSelected: viewModel.businessData.coreAttractions.contains(type)
                            ) {
                                toggleAttraction(type)
                            }
                        }
                    }
                }
                
                // 业态配比
                VStack(alignment: .leading, spacing: 16) {
                    Text("业态配比调整")
                        .font(.subheadline)
                        .fontWeight(.medium)
                    
                    VStack(spacing: 16) {
                        RatioSlider(
                            icon: "🍜",
                            title: "餐饮",
                            value: $viewModel.businessData.businessRatio.catering
                        )
                        RatioSlider(
                            icon: "🛍️",
                            title: "零售",
                            value: $viewModel.businessData.businessRatio.retail
                        )
                        RatioSlider(
                            icon: "🏨",
                            title: "住宿",
                            value: $viewModel.businessData.businessRatio.accommodation
                        )
                        RatioSlider(
                            icon: "🎮",
                            title: "娱乐",
                            value: $viewModel.businessData.businessRatio.entertainment
                        )
                        RatioSlider(
                            icon: "💁",
                            title: "服务",
                            value: $viewModel.businessData.businessRatio.service
                        )
                    }
                    .padding()
                    .background(Color.gray.opacity(0.05))
                    .cornerRadius(12)
                }
                
                // 动线设计
                SelectionSection(title: "游客动线设计") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 150))], spacing: 12) {
                        ForEach(CirculationType.allCases) { type in
                            SelectableCard(
                                icon: type.icon,
                                title: type.rawValue,
                                subtitle: type.description,
                                isSelected: viewModel.businessData.circulation == type
                            ) {
                                viewModel.businessData.circulation = type
                            }
                        }
                    }
                }
                
                // 运营指标
                VStack(alignment: .leading, spacing: 12) {
                    Text("运营指标")
                        .font(.subheadline)
                        .fontWeight(.medium)
                    
                    HStack(spacing: 12) {
                        PickerSection(title: "停留时长") {
                            Picker("", selection: $viewModel.businessData.stayDuration) {
                                Text("请选择").tag(nil as StayDuration?)
                                ForEach(StayDuration.allCases) { duration in
                                    Text(duration.rawValue).tag(duration as StayDuration?)
                                }
                            }
                        }
                        
                        PickerSection(title: "门票价格") {
                            Picker("", selection: $viewModel.businessData.ticketPrice) {
                                Text("请选择").tag(nil as TicketPrice?)
                                ForEach(TicketPrice.allCases) { price in
                                    Text(price.rawValue).tag(price as TicketPrice?)
                                }
                            }
                        }
                        
                        PickerSection(title: "年容量") {
                            Picker("", selection: $viewModel.businessData.annualCapacity) {
                                Text("请选择").tag(nil as AnnualCapacity?)
                                ForEach(AnnualCapacity.allCases) { capacity in
                                    Text(capacity.rawValue).tag(capacity as AnnualCapacity?)
                                }
                            }
                        }
                    }
                }
                
                // 按钮组
                HStack {
                    Button(action: viewModel.goToPreviousStep) {
                        HStack {
                            Image(systemName: "arrow.left")
                            Text("上一步")
                        }
                        .foregroundColor(.gray)
                        .padding(.horizontal, 20)
                        .padding(.vertical, 12)
                        .overlay(
                            RoundedRectangle(cornerRadius: 8)
                                .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                        )
                    }
                    .buttonStyle(PlainButtonStyle())
                    
                    Spacer()
                    
                    Button(action: viewModel.goToNextStep) {
                        HStack {
                            Text("下一步：运营策略")
                            Image(systemName: "arrow.right")
                        }
                        .fontWeight(.semibold)
                        .foregroundColor(.white)
                        .padding(.horizontal, 24)
                        .padding(.vertical, 12)
                        .background(Color.orange)
                        .cornerRadius(8)
                    }
                }
                .padding(.top, 16)
            }
            .padding()
        }
    }
    
    private func toggleAttraction(_ type: AttractionType) {
        if let index = viewModel.businessData.coreAttractions.firstIndex(of: type) {
            viewModel.businessData.coreAttractions.remove(at: index)
        } else {
            viewModel.businessData.coreAttractions.append(type)
        }
    }
}

// MARK: - 比例滑块
struct RatioSlider: View {
    let icon: String
    let title: String
    @Binding var value: Double
    
    var body: some View {
        HStack(spacing: 12) {
            Text(icon)
                .font(.title3)
            
            VStack(alignment: .leading, spacing: 4) {
                HStack {
                    Text(title)
                        .font(.subheadline)
                        .foregroundColor(.primary)
                    Spacer()
                    Text("\(Int(value))%")
                        .font(.subheadline)
                        .fontWeight(.bold)
                        .foregroundColor(.orange)
                }
                
                Slider(value: $value, in: 0...50, step: 5)
                    .accentColor(.orange)
            }
        }
    }
}

// MARK: - Picker 包装
struct PickerSection<Content: View>: View {
    let title: String
    @ViewBuilder let content: Content
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(title)
                .font(.caption)
                .foregroundColor(.gray)
            content
                .pickerStyle(MenuPickerStyle())
                .frame(maxWidth: .infinity)
                .padding(8)
                .background(Color.gray.opacity(0.1))
                .cornerRadius(8)
        }
        .frame(maxWidth: .infinity)
    }
}
