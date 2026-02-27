//
//  StyleSelector.swift
//  设计风格与团队选择
//

import SwiftUI

struct StyleSelector: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 25) {
                // 设计风格
                DesignStyleSection(project: project)
                
                Divider()
                
                // 设计团队
                DesignTeamSection(project: project)
                
                Divider()
                
                // 已选团队展示
                if !project.parameters.preferredTeams.isEmpty {
                    SelectedTeamsSection(project: project)
                }
            }
            .padding()
        }
    }
}

// MARK: - 设计风格选择
struct DesignStyleSection: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        VStack(alignment: .leading, spacing: 15) {
            Label("设计风格", systemImage: "paintpalette.fill")
                .font(.headline)
            
            LazyVGrid(columns: [GridItem(.adaptive(minimum: 140))], spacing: 12) {
                ForEach(DesignStyle.allCases) { style in
                    StyleCard(
                        style: style,
                        isSelected: project.parameters.designStyle == style
                    ) {
                        project.parameters.designStyle = style
                    }
                }
            }
        }
    }
}

struct StyleCard: View {
    let style: DesignStyle
    let isSelected: Bool
    let onTap: () -> Void
    
    var body: some View {
        Button(action: onTap) {
            VStack(alignment: .leading, spacing: 8) {
                HStack {
                    Image(systemName: style.icon)
                        .font(.title2)
                        .foregroundColor(isSelected ? .white : .accentColor)
                    Spacer()
                    if isSelected {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundColor(.white)
                    }
                }
                
                Text(style.rawValue)
                    .font(.subheadline)
                    .fontWeight(.semibold)
                    .foregroundColor(isSelected ? .white : .primary)
                
                Text(style.description)
                    .font(.caption)
                    .foregroundColor(isSelected ? .white.opacity(0.8) : .secondary)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
            }
            .padding()
            .frame(maxWidth: .infinity, minHeight: 100, alignment: .topLeading)
            .background(isSelected ? Color.accentColor : Color.gray.opacity(0.1))
            .cornerRadius(12)
        }
        .buttonStyle(PlainButtonStyle())
    }
}

// MARK: - 设计团队选择
struct DesignTeamSection: View {
    @ObservedObject var project: DesignProject
    @State private var selectedCountry: String = "全部"
    
    let countries = ["全部", "中国", "美国", "丹麦", "日本", "新加坡", "挪威", "英国"]
    
    var filteredTeams: [DesignTeam] {
        if selectedCountry == "全部" {
            return DesignTeam.allTeams
        } else {
            return DesignTeam.allTeams.filter { $0.country == selectedCountry }
        }
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 15) {
            HStack {
                Label("设计团队", systemImage: "person.3.fill")
                    .font(.headline)
                
                Spacer()
                
                Picker("国家", selection: $selectedCountry) {
                    ForEach(countries, id: \.self) { country in
                        Text(country).tag(country)
                    }
                }
                .pickerStyle(MenuPickerStyle())
                .frame(width: 120)
            }
            
            Text("选择你想要学习的顶尖设计团队（可多选）")
                .font(.caption)
                .foregroundColor(.secondary)
            
            LazyVGrid(columns: [GridItem(.adaptive(minimum: 280))], spacing: 12) {
                ForEach(filteredTeams) { team in
                    TeamCard(
                        team: team,
                        isSelected: project.parameters.preferredTeams.contains(where: { $0.id == team.id })
                    ) {
                        toggleTeam(team)
                    }
                }
            }
        }
    }
    
    private func toggleTeam(_ team: DesignTeam) {
        if let index = project.parameters.preferredTeams.firstIndex(where: { $0.id == team.id }) {
            project.parameters.preferredTeams.remove(at: index)
        } else {
            var mutableTeam = team
            mutableTeam.isSelected = true
            project.parameters.preferredTeams.append(mutableTeam)
        }
    }
}

struct TeamCard: View {
    let team: DesignTeam
    let isSelected: Bool
    let onTap: () -> Void
    
    var body: some View {
        Button(action: onTap) {
            VStack(alignment: .leading, spacing: 10) {
                HStack {
                    // 国旗emoji（简化版）
                    Text(flagEmoji(for: team.country))
                        .font(.title2)
                    
                    VStack(alignment: .leading, spacing: 2) {
                        Text(team.name)
                            .font(.subheadline)
                            .fontWeight(.semibold)
                            .foregroundColor(isSelected ? .white : .primary)
                        
                        Text(team.country)
                            .font(.caption)
                            .foregroundColor(isSelected ? .white.opacity(0.8) : .secondary)
                    }
                    
                    Spacer()
                    
                    if isSelected {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundColor(.white)
                    }
                }
                
                Text(team.specialty)
                    .font(.caption)
                    .foregroundColor(isSelected ? .white.opacity(0.9) : .secondary)
                
                Text(team.description)
                    .font(.caption)
                    .foregroundColor(isSelected ? .white.opacity(0.7) : .gray)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
                
                // 代表作品
                HStack(spacing: 4) {
                    ForEach(team.representativeWorks.prefix(2), id: \.self) { work in
                        Text(work)
                            .font(.caption2)
                            .padding(.horizontal, 6)
                            .padding(.vertical, 2)
                            .background(isSelected ? Color.white.opacity(0.2) : Color.gray.opacity(0.1))
                            .foregroundColor(isSelected ? .white : .secondary)
                            .cornerRadius(4)
                    }
                }
            }
            .padding()
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(isSelected ? Color.accentColor : Color.gray.opacity(0.1))
            .cornerRadius(12)
        }
        .buttonStyle(PlainButtonStyle())
    }
    
    private func flagEmoji(for country: String) -> String {
        switch country {
        case "中国": return "🇨🇳"
        case "美国": return "🇺🇸"
        case "丹麦": return "🇩🇰"
        case "日本": return "🇯🇵"
        case "新加坡": return "🇸🇬"
        case "挪威": return "🇳🇴"
        case "英国": return "🇬🇧"
        default: return "🌍"
        }
    }
}

// MARK: - 已选团队展示
struct SelectedTeamsSection: View {
    @ObservedObject var project: DesignProject
    
    var body: some View {
        VStack(alignment: .leading, spacing: 15) {
            Label("已选择的设计团队", systemImage: "checkmark.circle.fill")
                .font(.headline)
            
            VStack(alignment: .leading, spacing: 10) {
                ForEach(project.parameters.preferredTeams) { team in
                    HStack {
                        Text(flagEmoji(for: team.country))
                        Text(team.name)
                            .font(.subheadline)
                        Spacer()
                        Text(team.corePhilosophy)
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .lineLimit(1)
                    }
                    .padding(.vertical, 4)
                }
            }
            .padding()
            .background(Color.accentColor.opacity(0.1))
            .cornerRadius(8)
            
            // AI学习说明
            VStack(alignment: .leading, spacing: 8) {
                Label("AI将学习以下设计理念", systemImage: "brain.head.profile")
                    .font(.subheadline)
                    .fontWeight(.medium)
                
                ForEach(project.parameters.preferredTeams) { team in
                    HStack(alignment: .top) {
                        Text("•")
                        VStack(alignment: .leading, spacing: 2) {
                            Text("\(team.name): ")
                                .font(.caption)
                                .fontWeight(.medium)
                            Text(team.corePhilosophy)
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }
                    }
                }
            }
            .padding()
            .background(Color.gray.opacity(0.05))
            .cornerRadius(8)
        }
    }
    
    private func flagEmoji(for country: String) -> String {
        switch country {
        case "中国": return "🇨🇳"
        case "美国": return "🇺🇸"
        case "丹麦": return "🇩🇰"
        case "日本": return "🇯🇵"
        case "新加坡": return "🇸🇬"
        case "挪威": return "🇳🇴"
        case "英国": return "🇬🇧"
        default: return "🌍"
        }
    }
}
