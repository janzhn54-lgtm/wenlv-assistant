//
//  OperationView.swift
//  运营策略页面
//

import SwiftUI

struct OperationView: View {
    @ObservedObject var viewModel: PlanViewModel
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                // 标题
                VStack(alignment: .leading, spacing: 4) {
                    Text("⚡ 运营策略")
                        .font(.title2)
                        .fontWeight(.bold)
                    Text("制定四季运营、营销推广和社群运营策略")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                }
                
                // 四季运营
                SelectionSection(title: "重点发力季节（可多选）") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 140))], spacing: 12) {
                        ForEach(Season.allCases) { season in
                            SeasonCard(
                                season: season,
                                isSelected: viewModel.operationData.seasonFocus.contains(season)
                            ) {
                                toggleSeason(season)
                            }
                        }
                    }
                }
                
                // 营销渠道
                SelectionSection(title: "数字营销渠道（可多选）") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 160))], spacing: 12) {
                        ForEach(MarketingChannel.allCases) { channel in
                            MultiSelectableCard(
                                icon: channel.icon,
                                title: channel.rawValue,
                                subtitle: channel.description,
                                isSelected: viewModel.operationData.marketingChannels.contains(channel)
                            ) {
                                toggleChannel(channel)
                            }
                        }
                    }
                }
                
                // 社群运营
                SelectionSection(title: "社群运营体系（可多选）") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 160))], spacing: 12) {
                        ForEach(CommunityFeature.allCases) { feature in
                            CommunityCard(
                                feature: feature,
                                isSelected: viewModel.operationData.communityFeatures.contains(feature)
                            ) {
                                toggleCommunity(feature)
                            }
                        }
                    }
                }
                
                // IP 合作
                InputSection(title: "IP 联名/合作计划") {
                    TextEditor(text: $viewModel.operationData.ipCollaboration)
                        .frame(height: 80)
                        .overlay(
                            RoundedRectangle(cornerRadius: 8)
                                .stroke(Color.gray.opacity(0.2), lineWidth: 1)
                        )
                }
                
                // 差异化
                InputSection(title: "与竞品的差异化优势") {
                    TextEditor(text: $viewModel.operationData.differentiation)
                        .frame(height: 80)
                        .overlay(
                            RoundedRectangle(cornerRadius: 8)
                                .stroke(Color.gray.opacity(0.2), lineWidth: 1)
                        )
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
                            Text("生成策划方案")
                            Image(systemName: "wand.and.stars")
                        }
                        .fontWeight(.semibold)
                        .foregroundColor(.white)
                        .padding(.horizontal, 24)
                        .padding(.vertical, 12)
                        .background(
                            LinearGradient(
                                gradient: Gradient(colors: [.orange, .amber]),
                                startPoint: .leading,
                                endPoint: .trailing
                            )
                        )
                        .cornerRadius(8)
                    }
                }
                .padding(.top, 16)
            }
            .padding()
        }
    }
    
    private func toggleSeason(_ season: Season) {
        if let index = viewModel.operationData.seasonFocus.firstIndex(of: season) {
            viewModel.operationData.seasonFocus.remove(at: index)
        } else {
            viewModel.operationData.seasonFocus.append(season)
        }
    }
    
    private func toggleChannel(_ channel: MarketingChannel) {
        if let index = viewModel.operationData.marketingChannels.firstIndex(of: channel) {
            viewModel.operationData.marketingChannels.remove(at: index)
        } else {
            viewModel.operationData.marketingChannels.append(channel)
        }
    }
    
    private func toggleCommunity(_ feature: CommunityFeature) {
        if let index = viewModel.operationData.communityFeatures.firstIndex(of: feature) {
            viewModel.operationData.communityFeatures.remove(at: index)
        } else {
            viewModel.operationData.communityFeatures.append(feature)
        }
    }
}

// MARK: - 季节卡片
struct SeasonCard: View {
    let season: Season
    let isSelected: Bool
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 6) {
                HStack {
                    Text(season.icon)
                        .font(.title2)
                    Text(season.rawValue)
                        .font(.subheadline)
                        .fontWeight(.medium)
                    Spacer()
                }
                
                Text(season.theme)
                    .font(.caption)
                    .foregroundColor(.orange)
                
                HStack {
                    ForEach(season.activities, id: \.self) { activity in
                        Text(activity)
                            .font(.caption2)
                            .padding(.horizontal, 6)
                            .padding(.vertical, 2)
                            .background(Color.orange.opacity(0.1))
                            .foregroundColor(.orange)
                            .cornerRadius(4)
                    }
                }
            }
            .padding()
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(isSelected ? Color.orange.opacity(0.1) : Color.gray.opacity(0.05))
            .overlay(
                RoundedRectangle(cornerRadius: 12)
                    .stroke(isSelected ? Color.orange : Color.gray.opacity(0.2), lineWidth: isSelected ? 2 : 1)
            )
            .cornerRadius(12)
        }
        .buttonStyle(PlainButtonStyle())
    }
}

// MARK: - 社群卡片
struct CommunityCard: View {
    let feature: CommunityFeature
    let isSelected: Bool
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 6) {
                Text(feature.icon)
                    .font(.title2)
                Text(feature.rawValue)
                    .font(.subheadline)
                    .fontWeight(.medium)
                Text(feature.description)
                    .font(.caption)
                    .foregroundColor(.gray)
                
                HStack(spacing: 4) {
                    ForEach(feature.features, id: \.self) { f in
                        Text(f)
                            .font(.caption2)
                            .padding(.horizontal, 6)
                            .padding(.vertical, 2)
                            .background(Color.white)
                            .cornerRadius(4)
                    }
                }
            }
            .padding()
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(isSelected ? Color.orange.opacity(0.1) : Color.gray.opacity(0.05))
            .overlay(
                RoundedRectangle(cornerRadius: 12)
                    .stroke(isSelected ? Color.orange : Color.gray.opacity(0.2), lineWidth: isSelected ? 2 : 1)
            )
            .cornerRadius(12)
        }
        .buttonStyle(PlainButtonStyle())
    }
}
