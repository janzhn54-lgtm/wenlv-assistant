//
//  PositioningView.swift
//  项目定位页面
//

import SwiftUI

struct PositioningView: View {
    @ObservedObject var viewModel: PlanViewModel
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                // 标题
                VStack(alignment: .leading, spacing: 4) {
                    Text("🎯 项目定位")
                        .font(.title2)
                        .fontWeight(.bold)
                    Text("明确项目的文化基因、目标客群和差异化定位")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                }
                
                // 项目名称
                InputSection(title: "项目名称") {
                    TextField("例如：绍兴XX文旅综合体", text: $viewModel.positioningData.projectName)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                }
                
                // 地理位置
                InputSection(title: "项目位置") {
                    TextField("例如：浙江省绍兴市柯桥区", text: $viewModel.positioningData.location)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                }
                
                // 地域类型
                SelectionSection(title: "地域资源类型") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 150))], spacing: 12) {
                        ForEach(LocationType.allCases) { type in
                            SelectableCard(
                                icon: type.icon,
                                title: type.rawValue,
                                subtitle: type.description,
                                isSelected: viewModel.positioningData.locationType == type
                            ) {
                                viewModel.positioningData.locationType = type
                            }
                        }
                    }
                }
                
                // 目标客群
                SelectionSection(title: "目标客群（可多选）") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 160))], spacing: 12) {
                        ForEach(TargetGroup.allCases) { group in
                            MultiSelectableCard(
                                icon: group.icon,
                                title: group.rawValue,
                                subtitle: group.description,
                                isSelected: viewModel.positioningData.targetGroups.contains(group)
                            ) {
                                toggleTargetGroup(group)
                            }
                        }
                    }
                }
                
                // 定位类型
                SelectionSection(title: "项目定位类型") {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 160))], spacing: 12) {
                        ForEach(PositioningType.allCases) { type in
                            SelectableCard(
                                icon: type.icon,
                                title: type.rawValue,
                                subtitle: type.description,
                                isSelected: viewModel.positioningData.positioningType == type
                            ) {
                                viewModel.positioningData.positioningType = type
                            }
                        }
                    }
                }
                
                // 核心主题
                InputSection(title: "核心文化主题") {
                    TextField("例如：江南水韵、越国文化、黄酒文化...", text: $viewModel.positioningData.coreTheme)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                }
                
                // 竞品分析
                InputSection(title: "主要竞品/对标项目") {
                    TextEditor(text: $viewModel.positioningData.competitors)
                        .frame(height: 80)
                        .overlay(
                            RoundedRectangle(cornerRadius: 8)
                                .stroke(Color.gray.opacity(0.2), lineWidth: 1)
                        )
                }
                
                // 下一步按钮
                HStack {
                    Spacer()
                    Button(action: viewModel.goToNextStep) {
                        HStack {
                            Text("下一步：业态规划")
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
    
    private func toggleTargetGroup(_ group: TargetGroup) {
        if let index = viewModel.positioningData.targetGroups.firstIndex(of: group) {
            viewModel.positioningData.targetGroups.remove(at: index)
        } else {
            viewModel.positioningData.targetGroups.append(group)
        }
    }
}

// MARK: - 通用组件
struct InputSection<Content: View>: View {
    let title: String
    @ViewBuilder let content: Content
    
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(title)
                .font(.subheadline)
                .fontWeight(.medium)
                .foregroundColor(.primary)
            content
        }
    }
}

struct SelectionSection<Content: View>: View {
    let title: String
    @ViewBuilder let content: Content
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(title)
                .font(.subheadline)
                .fontWeight(.medium)
            content
        }
    }
}

struct SelectableCard: View {
    let icon: String
    let title: String
    let subtitle: String
    let isSelected: Bool
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 4) {
                Text(icon)
                    .font(.title2)
                Text(title)
                    .font(.subheadline)
                    .fontWeight(.medium)
                    .foregroundColor(.primary)
                Text(subtitle)
                    .font(.caption)
                    .foregroundColor(.gray)
                    .lineLimit(2)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding()
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

struct MultiSelectableCard: View {
    let icon: String
    let title: String
    let subtitle: String
    let isSelected: Bool
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            HStack {
                VStack(alignment: .leading, spacing: 4) {
                    Text(icon)
                        .font(.title2)
                    Text(title)
                        .font(.subheadline)
                        .fontWeight(.medium)
                        .foregroundColor(.primary)
                    Text(subtitle)
                        .font(.caption)
                        .foregroundColor(.gray)
                        .lineLimit(1)
                }
                
                Spacer()
                
                Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                    .foregroundColor(isSelected ? .orange : .gray)
                    .font(.title3)
            }
            .padding()
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
