//
//  ProfileView.swift
//  个人中心页面
//

import SwiftUI

struct ProfileView: View {
    @EnvironmentObject var newsStore: NewsStore
    @State private var showingSettings = false
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 24) {
                    // 用户信息头部
                    ProfileHeader()
                    
                    // 阅读统计
                    StatsSection(stats: newsStore.stats)
                    
                    // 功能列表
                    SettingsList()
                    
                    // 关于
                    AboutSection()
                }
                .padding(.vertical)
            }
            .navigationTitle("我的")
        }
    }
}

// MARK: - 用户头部
struct ProfileHeader: View {
    var body: some View {
        VStack(spacing: 12) {
            Image(systemName: "person.circle.fill")
                .font(.system(size: 80))
                .foregroundColor(.orange)
            
            Text("文旅人")
                .font(.title2)
                .fontWeight(.bold)
            
            Text("关注文旅，洞察行业")
                .font(.subheadline)
                .foregroundColor(.gray)
        }
        .padding()
    }
}

// MARK: - 统计区域
struct StatsSection: View {
    let stats: (total: Int, read: Int, favorites: Int)
    
    var body: some View {
        VStack(spacing: 16) {
            Text("阅读统计")
                .font(.headline)
                .frame(maxWidth: .infinity, alignment: .leading)
            
            HStack(spacing: 20) {
                StatCard(
                    icon: "newspaper",
                    title: "总资讯",
                    value: stats.total,
                    color: .blue
                )
                
                StatCard(
                    icon: "eye",
                    title: "已读",
                    value: stats.read,
                    color: .green
                )
                
                StatCard(
                    icon: "star",
                    title: "收藏",
                    value: stats.favorites,
                    color: .orange
                )
            }
        }
        .padding()
        .background(Color.gray.opacity(0.05))
        .cornerRadius(16)
        .padding(.horizontal)
    }
}

// MARK: - 统计卡片
struct StatCard: View {
    let icon: String
    let title: String
    let value: Int
    let color: Color
    
    var body: some View {
        VStack(spacing: 8) {
            Image(systemName: icon)
                .font(.title2)
                .foregroundColor(color)
            
            Text("\(value)")
                .font(.title)
                .fontWeight(.bold)
            
            Text(title)
                .font(.caption)
                .foregroundColor(.gray)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 16)
        .background(Color(.systemBackground))
        .cornerRadius(12)
    }
}

// MARK: - 设置列表
struct SettingsList: View {
    var body: some View {
        VStack(spacing: 0) {
            SettingRow(
                icon: "bell.fill",
                title: "推送通知",
                subtitle: "每日8:00推送精选资讯",
                color: .red
            )
            
            Divider().padding(.leading, 56)
            
            SettingRow(
                icon: "moon.fill",
                title: "深色模式",
                subtitle: "跟随系统",
                color: .indigo
            )
            
            Divider().padding(.leading, 56)
            
            SettingRow(
                icon: "tag.fill",
                title: "偏好设置",
                subtitle: "选择感兴趣的分类",
                color: .orange
            )
            
            Divider().padding(.leading, 56)
            
            SettingRow(
                icon: "arrow.clockwise",
                title: "数据同步",
                subtitle: "上次更新：刚刚",
                color: .blue
            )
        }
        .background(Color(.systemBackground))
        .cornerRadius(12)
        .padding(.horizontal)
    }
}

// MARK: - 设置行
struct SettingRow: View {
    let icon: String
    let title: String
    let subtitle: String
    let color: Color
    
    var body: some View {
        HStack(spacing: 16) {
            Image(systemName: icon)
                .font(.title3)
                .foregroundColor(.white)
                .frame(width: 36, height: 36)
                .background(color)
                .cornerRadius(8)
            
            VStack(alignment: .leading, spacing: 4) {
                Text(title)
                    .font(.body)
                
                Text(subtitle)
                    .font(.caption)
                    .foregroundColor(.gray)
            }
            
            Spacer()
            
            Image(systemName: "chevron.right")
                .foregroundColor(.gray)
                .font(.caption)
        }
        .padding()
    }
}

// MARK: - 关于区域
struct AboutSection: View {
    var body: some View {
        VStack(spacing: 12) {
            Text("文旅日报")
                .font(.headline)
            
            Text("Version 1.0.0")
                .font(.caption)
                .foregroundColor(.gray)
            
            Text("专为文旅从业者打造的资讯平台")
                .font(.caption)
                .foregroundColor(.gray)
                .multilineTextAlignment(.center)
            
            HStack(spacing: 20) {
                Link(destination: URL(string: "https://github.com/janzhn54-lgtm/wenlv-assistant")!) {
                    Image(systemName: "github")
                        .font(.title2)
                        .foregroundColor(.primary)
                }
                
                Link(destination: URL(string: "mailto:contact@example.com")!) {
                    Image(systemName: "envelope")
                        .font(.title2)
                        .foregroundColor(.primary)
                }
            }
            .padding(.top, 8)
        }
        .padding()
        .frame(maxWidth: .infinity)
        .background(Color.gray.opacity(0.05))
        .cornerRadius(12)
        .padding(.horizontal)
    }
}
