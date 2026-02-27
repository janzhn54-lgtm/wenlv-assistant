//
//  OutputView.swift
//  生成结果页面
//

import SwiftUI
import UniformTypeIdentifiers

struct OutputView: View {
    @ObservedObject var viewModel: PlanViewModel
    @State private var showingShareSheet = false
    @State private var exportFormat: ExportFormat = .markdown
    
    enum ExportFormat {
        case markdown
        case text
    }
    
    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                if viewModel.isGenerating {
                    GeneratingView()
                } else if let plan = viewModel.generatedPlan {
                    PlanResultView(plan: plan, viewModel: viewModel)
                } else {
                    GeneratePromptView(viewModel: viewModel)
                }
            }
            .padding()
        }
    }
}

// MARK: - 生成中视图
struct GeneratingView: View {
    var body: some View {
        VStack(spacing: 20) {
            Spacer()
            
            Text("📄")
                .font(.system(size: 80))
            
            Text("正在生成策划方案...")
                .font(.title2)
                .fontWeight(.bold)
            
            ProgressView()
                .scaleEffect(1.5)
                .padding()
            
            Spacer()
        }
        .frame(maxWidth: .infinity, minHeight: 400)
    }
}

// MARK: - 生成提示视图
struct GeneratePromptView: View {
    @ObservedObject var viewModel: PlanViewModel
    
    var body: some View {
        VStack(spacing: 24) {
            Spacer()
            
            Text("📄")
                .font(.system(size: 80))
            
            Text("生成策划方案")
                .font(.title2)
                .fontWeight(.bold)
            
            Text("基于你填写的项目定位、业态规划和运营策略，AI 将生成一份完整的文旅策划方案")
                .font(.subheadline)
                .foregroundColor(.gray)
                .multilineTextAlignment(.center)
                .padding(.horizontal)
            
            Button(action: viewModel.generatePlan) {
                HStack {
                    Image(systemName: "wand.and.stars")
                    Text("一键生成方案")
                }
                .font(.headline)
                .foregroundColor(.white)
                .padding(.horizontal, 32)
                .padding(.vertical, 16)
                .background(
                    LinearGradient(
                        gradient: Gradient(colors: [.orange, .amber]),
                        startPoint: .leading,
                        endPoint: .trailing
                    )
                )
                .cornerRadius(12)
                .shadow(radius: 4)
            }
            
            Spacer()
        }
        .frame(maxWidth: .infinity, minHeight: 400)
    }
}

// MARK: - 方案结果视图
struct PlanResultView: View {
    let plan: PlanResult
    @ObservedObject var viewModel: PlanViewModel
    @State private var showingShareSheet = false
    @State private var exportText = ""
    @State private var showingCopyAlert = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            // 头部
            HStack {
                VStack(alignment: .leading, spacing: 4) {
                    Text(plan.title)
                        .font(.title2)
                        .fontWeight(.bold)
                    Text("策划方案已生成")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                }
                
                Spacer()
                
                Menu {
                    Button(action: { shareAsMarkdown() }) {
                        Label("导出 Markdown", systemImage: "doc.text")
                    }
                    Button(action: { shareAsText() }) {
                        Label("导出文本", systemImage: "text.quote")
                    }
                    Button(action: {
                        UIPasteboard.general.string = plan.toMarkdown()
                        showingCopyAlert = true
                    }) {
                        Label("复制到剪贴板", systemImage: "doc.on.doc")
                    }
                } label: {
                    Image(systemName: "square.and.arrow.up")
                        .font(.title2)
                        .foregroundColor(.orange)
                }
            }
            
            // 项目概述
            SummaryCard(summary: plan.summary)
            
            // 项目定位
            PositioningSection(data: plan.positioning)
            
            // 业态规划
            BusinessSection(data: plan.business)
            
            // 运营策略
            OperationSection(data: plan.operation)
            
            // 底部按钮
            HStack {
                Button(action: viewModel.goToPreviousStep) {
                    HStack {
                        Image(systemName: "arrow.left")
                        Text("返回修改")
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
                
                Button(action: viewModel.reset) {
                    HStack {
                        Image(systemName: "arrow.counterclockwise")
                        Text("重新生成")
                    }
                    .foregroundColor(.orange)
                    .padding(.horizontal, 20)
                    .padding(.vertical, 12)
                    .background(Color.orange.opacity(0.1))
                    .cornerRadius(8)
                }
            }
        }
        .sheet(isPresented: $showingShareSheet) {
            ShareSheet(activityItems: [exportText])
        }
        .alert("已复制到剪贴板", isPresented: $showingCopyAlert) {
            Button("确定", role: .cancel) {}
        }
    }
    
    private func shareAsMarkdown() {
        exportText = plan.toMarkdown()
        showingShareSheet = true
    }
    
    private func shareAsText() {
        exportText = plan.toText()
        showingShareSheet = true
    }
}

// MARK: - 概述卡片
struct SummaryCard: View {
    let summary: String
    
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("📝 项目概述")
                .font(.headline)
            Text(summary)
                .font(.body)
                .foregroundColor(.primary)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color.orange.opacity(0.1))
        .cornerRadius(12)
    }
}

// MARK: - 定位部分
struct PositioningSection: View {
    let data: PositioningData
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("一、项目定位")
                .font(.headline)
                .padding(.bottom, 4)
            
            InfoGrid(items: [
                ("地理位置", data.location.isEmpty ? "待定" : data.location),
                ("资源类型", data.locationType?.rawValue ?? "待定"),
                ("目标客群", data.targetGroups.map(\\.rawValue).joined(separator: "、").isEmpty ? "待定" : data.targetGroups.map(\\.rawValue).joined(separator: "、")),
                ("项目定位", data.positioningType?.rawValue ?? "待定")
            ])
            
            InfoRow(title: "核心文化主题", value: data.coreTheme.isEmpty ? "待定" : data.coreTheme)
            
            if !data.competitors.isEmpty {
                InfoRow(title: "竞品分析", value: data.competitors)
            }
        }
        .padding()
        .background(Color.gray.opacity(0.05))
        .cornerRadius(12)
    }
}

// MARK: - 业态部分
struct BusinessSection: View {
    let data: BusinessData
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("二、业态规划")
                .font(.headline)
                .padding(.bottom, 4)
            
            if !data.coreAttractions.isEmpty {
                VStack(alignment: .leading, spacing: 8) {
                    Text("核心吸引物")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                    FlowLayout(spacing: 8) {
                        ForEach(data.coreAttractions, id: \.self) { attraction in
                            Tag(text: attraction.rawValue, color: .orange)
                        }
                    }
                }
            }
            
            VStack(alignment: .leading, spacing: 12) {
                Text("业态配比")
                    .font(.subheadline)
                    .foregroundColor(.gray)
                
                VStack(spacing: 8) {
                    RatioBar(icon: "🍜", label: "餐饮", value: data.businessRatio.catering, color: .orange)
                    RatioBar(icon: "🛍️", label: "零售", value: data.businessRatio.retail, color: .blue)
                    RatioBar(icon: "🏨", label: "住宿", value: data.businessRatio.accommodation, color: .green)
                    RatioBar(icon: "🎮", label: "娱乐", value: data.businessRatio.entertainment, color: .purple)
                    RatioBar(icon: "💁", label: "服务", value: data.businessRatio.service, color: .gray)
                }
            }
            
            InfoGrid(items: [
                ("动线设计", data.circulation?.rawValue ?? "待定"),
                ("停留时长", data.stayDuration?.rawValue ?? "待定"),
                ("门票价格", data.ticketPrice?.rawValue ?? "待定")
            ])
        }
        .padding()
        .background(Color.gray.opacity(0.05))
        .cornerRadius(12)
    }
}

// MARK: - 运营部分
struct OperationSection: View {
    let data: OperationData
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("三、运营策略")
                .font(.headline)
                .padding(.bottom, 4)
            
            if !data.seasonFocus.isEmpty {
                VStack(alignment: .leading, spacing: 8) {
                    Text("四季运营重点")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                    FlowLayout(spacing: 8) {
                        ForEach(data.seasonFocus, id: \.self) { season in
                            Tag(text: "\(season.icon) \(season.rawValue)(\(season.theme))", color: .green)
                        }
                    }
                }
            }
            
            VStack(alignment: .leading, spacing: 8) {
                Text("营销渠道")
                    .font(.subheadline)
                    .foregroundColor(.gray)
                FlowLayout(spacing: 8) {
                    ForEach(data.marketingChannels, id: \.self) { channel in
                        Tag(text: channel.rawValue, color: .blue)
                    }
                }
            }
            
            if !data.communityFeatures.isEmpty {
                VStack(alignment: .leading, spacing: 8) {
                    Text("社群运营")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                    FlowLayout(spacing: 8) {
                        ForEach(data.communityFeatures, id: \.self) { feature in
                            Tag(text: feature.rawValue, color: .purple)
                        }
                    }
                }
            }
            
            if !data.differentiation.isEmpty {
                InfoRow(title: "差异化优势", value: data.differentiation, highlight: true)
            }
        }
        .padding()
        .background(Color.gray.opacity(0.05))
        .cornerRadius(12)
    }
}

// MARK: - 辅助组件
struct InfoGrid: View {
    let items: [(String, String)]
    
    var body: some View {
        LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 12) {
            ForEach(items, id: \.0) { item in
                VStack(alignment: .leading, spacing: 4) {
                    Text(item.0)
                        .font(.caption)
                        .foregroundColor(.gray)
                    Text(item.1)
                        .font(.subheadline)
                        .fontWeight(.medium)
                }
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding()
                .background(Color.gray.opacity(0.1))
                .cornerRadius(8)
            }
        }
    }
}

struct InfoRow: View {
    let title: String
    let value: String
    var highlight: Bool = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(title)
                .font(.caption)
                .foregroundColor(.gray)
            Text(value)
                .font(.subheadline)
                .fontWeight(.medium)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding()
        .background(highlight ? Color.orange.opacity(0.1) : Color.gray.opacity(0.1))
        .cornerRadius(8)
    }
}

struct RatioBar: View {
    let icon: String
    let label: String
    let value: Double
    let color: Color
    
    var body: some View {
        HStack(spacing: 12) {
            Text(icon)
                .font(.title3)
            Text(label)
                .font(.subheadline)
                .frame(width: 50, alignment: .leading)
            
            GeometryReader { geometry in
                ZStack(alignment: .leading) {
                    Rectangle()
                        .fill(Color.gray.opacity(0.2))
                        .cornerRadius(4)
                    
                    Rectangle()
                        .fill(color)
                        .frame(width: geometry.size.width * CGFloat(value / 100))
                        .cornerRadius(4)
                }
            }
            .frame(height: 16)
            
            Text("\(Int(value))%")
                .font(.subheadline)
                .fontWeight(.bold)
                .frame(width: 45, alignment: .trailing)
        }
    }
}

struct Tag: View {
    let text: String
    let color: Color
    
    var body: some View {
        Text(text)
            .font(.caption)
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .background(color.opacity(0.15))
            .foregroundColor(color)
            .cornerRadius(12)
    }
}

// MARK: - 流式布局
struct FlowLayout: Layout {
    var spacing: CGFloat = 8
    
    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let result = FlowResult(in: proposal.width ?? 0, subviews: subviews, spacing: spacing)
        return result.size
    }
    
    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        let result = FlowResult(in: bounds.width, subviews: subviews, spacing: spacing)
        for (index, subview) in subviews.enumerated() {
            subview.place(at: CGPoint(x: bounds.minX + result.positions[index].x,
                                      y: bounds.minY + result.positions[index].y),
                         proposal: .unspecified)
        }
    }
    
    struct FlowResult {
        var size: CGSize = .zero
        var positions: [CGPoint] = []
        
        init(in maxWidth: CGFloat, subviews: Subviews, spacing: CGFloat) {
            var x: CGFloat = 0
            var y: CGFloat = 0
            var lineHeight: CGFloat = 0
            
            for subview in subviews {
                let size = subview.sizeThatFits(.unspecified)
                
                if x + size.width > maxWidth && x > 0 {
                    x = 0
                    y += lineHeight + spacing
                    lineHeight = 0
                }
                
                positions.append(CGPoint(x: x, y: y))
                lineHeight = max(lineHeight, size.height)
                x += size.width + spacing
            }
            
            self.size = CGSize(width: maxWidth, height: y + lineHeight)
        }
    }
}

// MARK: - 分享Sheet
struct ShareSheet: UIViewControllerRepresentable {
    let activityItems: [Any]
    
    func makeUIViewController(context: Context) -> UIActivityViewController {
        let controller = UIActivityViewController(activityItems: activityItems, applicationActivities: nil)
        return controller
    }
    
    func updateUIViewController(_ uiViewController: UIActivityViewController, context: Context) {}
}
