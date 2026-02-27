//
//  ParametersEditor.swift
//  参数编辑器
//

import SwiftUI

struct ParametersEditor: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 25) {
                // 功能类型选择
                FunctionTypeSection(project: project)
                
                Divider()
                
                // 规划指标
                PlanningIndicatorsSection(project: project)
                
                Divider()
                
                // 用地信息
                LandInfoSection(project: project)
            }
            .padding()
        }
    }
}

// MARK: - 功能类型选择
struct FunctionTypeSection: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        VStack(alignment: .leading, spacing: 15) {
            Label("功能定位", systemImage: "building.2.fill")
                .font(.headline)
            
            LazyVGrid(columns: [GridItem(.adaptive(minimum: 150))], spacing: 12) {
                ForEach(FunctionType.allCases) { type in
                    FunctionTypeCard(
                        type: type,
                        isSelected: project.parameters.functionType == type
                    ) {
                        project.parameters.functionType = type
                        // 自动更新默认容积率
                        project.parameters.plotRatio = type.defaultPlotRatio
                    }
                }
            }
        }
    }
}

struct FunctionTypeCard: View {
    let type: FunctionType
    let isSelected: Bool
    let onTap: () -> Void
    
    var body: some View {
        Button(action: onTap) {
            VStack(alignment: .leading, spacing: 8) {
                HStack {
                    Image(systemName: type.icon)
                        .font(.title2)
                        .foregroundColor(isSelected ? .white : .accentColor)
                    Spacer()
                    if isSelected {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundColor(.white)
                    }
                }
                
                Text(type.rawValue)
                    .font(.subheadline)
                    .fontWeight(.semibold)
                    .foregroundColor(isSelected ? .white : .primary)
                
                Text(type.description)
                    .font(.caption)
                    .foregroundColor(isSelected ? .white.opacity(0.8) : .secondary)
                    .lineLimit(2)
            }
            .padding()
            .frame(maxWidth: .infinity, minHeight: 100, alignment: .topLeading)
            .background(isSelected ? Color.accentColor : Color.gray.opacity(0.1))
            .cornerRadius(12)
        }
        .buttonStyle(PlainButtonStyle())
    }
}

// MARK: - 规划指标
struct PlanningIndicatorsSection: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Label("规划指标", systemImage: "slider.horizontal.3")
                .font(.headline)
            
            VStack(spacing: 20) {
                // 容积率
                ParameterSlider(
                    title: "容积率",
                    value: $project.parameters.plotRatio,
                    range: 0.5...5.0,
                    step: 0.1,
                    unit: "",
                    description: "总建筑面积/用地面积"
                )
                
                // 建筑密度
                ParameterSlider(
                    title: "建筑密度",
                    value: $project.parameters.buildingDensity,
                    range: 10...60,
                    step: 1,
                    unit: "%",
                    description: "建筑基底面积占比"
                )
                
                // 绿化率
                ParameterSlider(
                    title: "绿化率",
                    value: $project.parameters.greenRate,
                    range: 10...50,
                    step: 1,
                    unit: "%",
                    description: "绿地面积占比"
                )
                
                // 限高
                ParameterSlider(
                    title: "限高",
                    value: $project.parameters.heightLimit,
                    range: 6...150,
                    step: 3,
                    unit: "m",
                    description: "建筑最大高度"
                )
                
                // 停车标准
                ParameterSlider(
                    title: "停车标准",
                    value: $project.parameters.parkingStandard,
                    range: 0.3...2.0,
                    step: 0.1,
                    unit: "车位/100㎡",
                    description: "单位建筑面积车位数"
                )
            }
        }
    }
}

struct ParameterSlider: View {
    let title: String
    @Binding var value: Double
    let range: ClosedRange<Double>
    let step: Double
    let unit: String
    let description: String
    
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Text(title)
                    .font(.subheadline)
                    .fontWeight(.medium)
                
                Spacer()
                
                Text(String(format: "%.1f%@", value, unit))
                    .font(.subheadline)
                    .fontWeight(.bold)
                    .foregroundColor(.accentColor)
                    .frame(minWidth: 80, alignment: .trailing)
            }
            
            Slider(value: $value, in: range, step: step)
                .accentColor(.accentColor)
            
            HStack {
                Text(String(format: "%.1f", range.lowerBound))
                    .font(.caption)
                    .foregroundColor(.secondary)
                
                Spacer()
                
                Text(description)
                    .font(.caption)
                    .foregroundColor(.secondary)
                
                Spacer()
                
                Text(String(format: "%.1f", range.upperBound))
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
        }
        .padding()
        .background(Color.gray.opacity(0.05))
        .cornerRadius(8)
    }
}

// MARK: - 用地信息
struct LandInfoSection: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        VStack(alignment: .leading, spacing: 15) {
            Label("用地信息", systemImage: "ruler.fill")
                .font(.headline)
            
            if project.inputData.landArea > 0 {
                VStack(spacing: 12) {
                    InfoRow(title: "用地面积", value: String(format: "%.2f ㎡", project.inputData.landArea))
                    InfoRow(title: "约", value: String(format: "%.2f 公顷", project.inputData.landArea / 10000))
                    InfoRow(title: "约", value: String(format: "%.2f 亩", project.inputData.landArea / 666.67))
                    
                    Divider()
                    
                    // 计算指标
                    let maxBuildingArea = project.inputData.landArea * project.parameters.plotRatio
                    InfoRow(title: "最大建筑面积", value: String(format: "%.0f ㎡", maxBuildingArea))
                    
                    let maxGreenArea = project.inputData.landArea * project.parameters.greenRate / 100
                    InfoRow(title: "最小绿地面积", value: String(format: "%.0f ㎡", maxGreenArea))
                    
                    let maxBuildingFootprint = project.inputData.landArea * project.parameters.buildingDensity / 100
                    InfoRow(title: "最大建筑占地", value: String(format: "%.0f ㎡", maxBuildingFootprint))
                }
            } else {
                Text("请先导入规划范围文件")
                    .foregroundColor(.secondary)
                    .frame(maxWidth: .infinity, alignment: .center)
                    .padding()
            }
        }
    }
}

struct InfoRow: View {
    let title: String
    let value: String
    
    var body: some View {
        HStack {
            Text(title)
                .font(.subheadline)
                .foregroundColor(.secondary)
            
            Spacer()
            
            Text(value)
                .font(.subheadline)
                .fontWeight(.medium)
        }
    }
}
