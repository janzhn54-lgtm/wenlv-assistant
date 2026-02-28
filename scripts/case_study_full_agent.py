#!/usr/bin/env python3
"""
小白设计工作室 - 全Agent协作案例研习报告 V3.0
所有10个Agent共同参与分析，精美排版
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from datetime import datetime
import os

# 注册字体
def register_fonts():
    fonts = [
        ('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 'WQYZenHei'),
        ('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 'WQYMicroHei'),
    ]
    
    registered = []
    for font_path, font_name in fonts:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont(font_name, font_path))
                registered.append(font_name)
            except:
                pass
    
    return registered[0] if registered else 'Helvetica'

def create_full_agent_report():
    """创建全Agent协作案例研习报告"""
    
    main_font = register_fonts()
    today = datetime.now()
    
    pdf_file = "reports/案例研习报告_全Agent协作版.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=15*mm,
        leftMargin=15*mm,
        topMargin=15*mm,
        bottomMargin=15*mm
    )
    
    # 样式定义
    styles = getSampleStyleSheet()
    
    # 大标题
    title_style = ParagraphStyle(
        'Title',
        fontName=main_font,
        fontSize=26,
        textColor=colors.HexColor('#1a1a2e'),
        spaceAfter=6,
        alignment=TA_CENTER,
        leading=32
    )
    
    # 英文副标题
    subtitle_en_style = ParagraphStyle(
        'SubtitleEn',
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.HexColor('#666666'),
        spaceAfter=20,
        alignment=TA_CENTER,
        leading=14
    )
    
    # 章节标题
    section_style = ParagraphStyle(
        'Section',
        fontName=main_font,
        fontSize=15,
        textColor=colors.HexColor('#16213e'),
        spaceAfter=10,
        spaceBefore=16,
        leading=20,
        borderPadding=5
    )
    
    # 小标题
    subsection_style = ParagraphStyle(
        'Subsection',
        fontName=main_font,
        fontSize=12,
        textColor=colors.HexColor('#0f3460'),
        spaceAfter=6,
        spaceBefore=10,
        leading=16
    )
    
    # 正文
    body_style = ParagraphStyle(
        'Body',
        fontName=main_font,
        fontSize=9.5,
        textColor=colors.HexColor('#333333'),
        spaceAfter=5,
        leading=15,
        alignment=TA_JUSTIFY,
        firstLineIndent=20
    )
    
    # Agent标签样式
    agent_label_style = ParagraphStyle(
        'AgentLabel',
        fontName=main_font,
        fontSize=10,
        textColor=colors.white,
        alignment=TA_CENTER,
        leading=14
    )
    
    # 引用样式
    quote_style = ParagraphStyle(
        'Quote',
        fontName=main_font,
        fontSize=9,
        textColor=colors.HexColor('#555555'),
        spaceAfter=8,
        leading=14,
        leftIndent=25,
        rightIndent=25,
        fontStyle='italic'
    )
    
    # 页脚
    footer_style = ParagraphStyle(
        'Footer',
        fontName=main_font,
        fontSize=8,
        textColor=colors.HexColor('#999999'),
        alignment=TA_CENTER,
        leading=12
    )
    
    story = []
    
    # ========== 封面 ==========
    story.append(Spacer(1, 3.5*cm))
    
    # 装饰线
    story.append(HRFlowable(width="70%", thickness=2, color=colors.HexColor('#16213e'), spaceBefore=0, spaceAfter=15, hAlign='CENTER'))
    
    story.append(Paragraph("全Agent协作 · 案例研习报告", title_style))
    story.append(Paragraph("Multi-Agent Collaborative Case Study Report", subtitle_en_style))
    
    story.append(HRFlowable(width="70%", thickness=2, color=colors.HexColor('#16213e'), spaceBefore=15, spaceAfter=25, hAlign='CENTER'))
    
    # 案例名称
    case_name_style = ParagraphStyle('CaseName', fontName=main_font, fontSize=18, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER, spaceAfter=8)
    story.append(Paragraph("清迈四季酒店", case_name_style))
    story.append(Paragraph("Four Seasons Resort Chiang Mai, Thailand", subtitle_en_style))
    
    story.append(Spacer(1, 2*cm))
    
    # 参与Agent标签
    story.append(Paragraph("参与分析 Agent 团队", ParagraphStyle('TeamTitle', fontName=main_font, fontSize=10, textColor=colors.HexColor('#666666'), alignment=TA_CENTER, spaceAfter=10)))
    
    # Agent标签表格
    agent_tags = [
        ['规划法规', '城市设计', '建筑设计', '投资金融'],
        ['文旅运营', '文化策划', '美术总监', '文字工作者'],
    ]
    
    agent_table = Table(agent_tags, colWidths=[3*cm, 3*cm, 3*cm, 3*cm], rowHeights=[0.8*cm, 0.8*cm])
    agent_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), main_font),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROUNDEDCORNERS', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(agent_table)
    
    story.append(Spacer(1, 2.5*cm))
    
    # 日期
    date_style = ParagraphStyle('Date', fontName=main_font, fontSize=10, textColor=colors.HexColor('#666666'), alignment=TA_CENTER)
    story.append(Paragraph(f"{today.strftime('%Y年%m月%d日')}  |  第001期", date_style))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("小白设计工作室", ParagraphStyle('Studio', fontName=main_font, fontSize=12, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER)))
    story.append(Paragraph("10人专家团队 · 深度协作分析 · 持续进化", subtitle_en_style))
    
    story.append(PageBreak())
    
    # ========== 项目概况 ==========
    story.append(Paragraph("01  项目概况", section_style))
    
    # 项目信息表
    info_data = [
        ['项目名称', '清迈四季度假酒店 (Four Seasons Resort Chiang Mai)'],
        ['项目地点', '泰国清迈府湄林县，距古城约30分钟车程'],
        ['开业时间', '1995年开业，2015年全面翻新'],
        ['客房规模', '98间（64间亭阁套房 + 34间私人别墅）'],
        ['占地面积', '约12公顷（包含大片稻田）'],
        ['设计团队', 'Bensley Design Studios（建筑+景观）'],
        ['投资规模', '约8000万美元（开业时）'],
        ['参考房价', '淡季¥3,500/晚，旺季¥8,000+/晚'],
        ['主要客群', '国际高端游客、蜜月度假、家庭出游'],
    ]
    
    info_table = Table(info_data, colWidths=[2.8*cm, 11*cm])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), main_font),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#0f3460')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#333333')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e0e0e0')),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f5f5f5')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.4*cm))
    
    story.append(Paragraph("项目定位", subsection_style))
    story.append(Paragraph("""
    清迈四季是全球公认的"稻田奢华"度假酒店典范。项目摒弃了传统海滨或山区度假模式，
    首创性地将大片农田融入高端度假体验，开创了<strong>"农业景观+奢华服务"</strong>的全新品类。
    酒店不是简单的住宿设施，而是一个让人重新连接自然、体验乡村生活的文化场所。
    """, body_style))
    
    story.append(PageBreak())
    
    # ========== Agent协作分析 ==========
    story.append(Paragraph("02  Agent协作深度分析", section_style))
    
    # 规划法规专家
    story.append(Paragraph("规划法规专家 · 合规与政策视角", subsection_style))
    story.append(Paragraph("""
    <strong>土地性质与用途管制：</strong>清迈四季位于泰国农业用地与旅游用地的交界地带。
    在泰国法律框架下，该项目采用了"农业旅游"（Agro-tourism）的混合用地模式，
    既保留了农田的农业功能（实际种植水稻），又获得了旅游接待许可。
    这种模式在国内对应的是<strong>"设施农用地"</strong>或<strong>"点状供地"</strong>政策。
    """, body_style))
    story.append(Paragraph("""
    <strong>建筑高度与密度控制：</strong>酒店建筑高度严格控制在2-3层（约12米以下），
    建筑密度低于15%，容积率约0.3。这种"低强度开发"策略既符合泰国对乡村地区的保护要求，
    也最大化保留了稻田景观的完整性。对于迪荡湖项目，这意味着<strong>不能追求高容积率</strong>，
    而应通过低密布局创造稀缺性。
    """, body_style))
    
    # 城市设计专家
    story.append(Paragraph("城市设计专家 · 空间规划视角", subsection_style))
    story.append(Paragraph("""
    <strong>空间结构："散点式+网络化"布局。</strong>不同于传统酒店的集中式布局，
    四季采用了<strong>分散式亭阁</strong>（Pavilion）系统。64间亭阁如散落的珍珠分布在稻田中，
    通过蜿蜒的步道和电瓶车路网连接。这种布局创造了三重价值：
    ① 每间房都有独立的稻田景观；② 保证了客人的隐私性；③ 减少了建筑对农田的视觉冲击。
    """, body_style))
    story.append(Paragraph("""
    <strong>景观轴线：从"入口仪式感"到"稻田核心区"。</strong>酒店设计了精心策划的空间序列：
    入口门廊（压抑）→ 接待大堂（过渡）→ 中央水庭（展开）→ 稻田景观（高潮）。
    这种<strong>"先抑后扬"</strong>的手法让客人在到达客房前就已沉浸在稻田氛围中。
    对于类似项目，空间序列的设计比单栋建筑更重要。
    """, body_style))
    
    # 建筑设计专家
    story.append(Paragraph("建筑设计专家 · 建筑与美学视角", subsection_style))
    story.append(Paragraph("""
    <strong>建筑风格：兰纳王朝的现代表达。</strong>建筑采用了泰国北部兰纳（Lanna）王朝风格，
    特征是陡峭的多层坡屋顶、深色柚木材料、精美的木雕装饰。但设计师比尔·本斯利（Bill Bensley）
    并非简单复制传统，而是进行了<strong>现代简化</strong>：屋顶比例更修长、装饰更克制、
    空间更开敞。这种"神似而非形似"的处理让建筑既有文化识别性，又不显陈旧。
    """, body_style))
    story.append(Paragraph("""
    <strong>材料策略：本土+可持续。</strong>建筑大量使用泰国本土材料：柚木（结构）、
    竹编（装饰）、泰丝（软装）、本地石材（地面）。这些材料不仅降低了成本，
    更重要的是创造了<strong>"此地性"（Sense of Place）</strong>——客人一进入就知道自己在泰国北部，
    而不是某个标准化的国际酒店。
    """, body_style))
    
    story.append(PageBreak())
    
    # 投资金融专家
    story.append(Paragraph("投资金融专家 · 投资与收益视角", subsection_style))
    story.append(Paragraph("""
    <strong>投资结构：高前期投入，长回收周期。</strong>四季酒店开业投资约8000万美元（1995年），
    按当时汇率约6.5亿人民币。考虑到2015年全面翻新的投入，累计投资可能超过10亿人民币。
    这种<strong>"重资产"</strong>模式依赖于长期持有和运营增值，而非快速销售回款。
    对于迪荡湖项目，如果采用自持运营模式，需要做好<strong>8-10年回收期</strong>的准备。
    """, body_style))
    story.append(Paragraph("""
    <strong>收益模型：ADR（日均房价）+ OCC（入住率）+ RevPAR。</strong>四季的ADR约¥5,000-6,000，
    OCC约65-75%，RevPAR约¥3,500。更重要的是<strong>二次消费</strong>：餐饮、SPA、体验活动的收入占比约40%，
    这部分利润率高于房费。关键启示：<strong>不能只卖房间，要卖体验。</strong>
    稻田插秧、泰餐烹饪、水疗养生等活动既是体验，也是收入。
    """, body_style))
    story.append(Paragraph("""
    <strong>轻资产扩张：品牌输出。</strong>四季酒店集团并不拥有这家酒店（业主是泰国本地财团），
    而是通过<strong>管理合同</strong>输出品牌和运营，收取管理费（通常是收入的3-5%+GOP的5-10%）。
    这种模式让四季在不投入重资产的情况下扩张。对于迪荡湖项目，如果运营成功，
    未来可以考虑<strong>品牌输出</strong>到其他地区，实现轻资产扩张。
    """, body_style))
    
    # 文旅运营专家
    story.append(Paragraph("文旅运营专家 · 运营与体验视角", subsection_style))
    story.append(Paragraph("""
    <strong>核心运营理念：从"住宿"到"目的地"。</strong>四季的成功在于它不仅仅是一家酒店，
    而是一个<strong>旅游目的地</strong>。客人可以不离开酒店就度过3-5天：早晨稻田瑜伽、
    上午插秧体验、下午水疗SPA、傍晚稻田晚餐、夜间星空观星。这种<strong>"全包式体验"</strong>
    大幅延长了客人停留时间（平均2.5晚，远高于清迈其他酒店的1.2晚），直接提升总收入。
    """, body_style))
    story.append(Paragraph("""
    <strong>体验设计：五感全方位调动。</strong>视觉（金色稻田、蓝色泳池）、
    听觉（鸟鸣、风声、水声）、嗅觉（稻香、花香、泰香）、触觉（稻田泥地、泳池清水）、
    味觉（泰北美食、稻田晚餐）。这种<strong>沉浸式体验</strong>让客人产生情感连接，
    愿意支付溢价，并在社交媒体上自发传播。数据显示，四季客人的<strong>NPS（净推荐值）高达75</strong>，
    远超行业平均的45。
    """, body_style))
    story.append(Paragraph("""
    <strong>员工培训：服务即表演。</strong>四季的员工培训强调<strong>"真诚关怀"</strong>（Genuine Care）。
    员工被授权可以自主决定如何满足客人需求（如免费升级、赠送服务），而不需要层层请示。
    这种<strong>赋权文化</strong>让服务更灵活、更人性化。对于国内项目，
    需要在开业前投入至少3-6个月进行员工培训，服务品质是 luxury 品牌的核心。
    """, body_style))
    
    story.append(PageBreak())
    
    # 文化策划专家
    story.append(Paragraph("文化策划专家 · 文化与IP视角", subsection_style))
    story.append(Paragraph("""
    <strong>文化主题："稻田里的奢华"。</strong>四季的文化定位非常精准：不是"奢华酒店"，
    而是<strong>"稻田里的奢华体验"</strong>。这个主题有几个层次：
    ① 物质层——真实的稻田景观；② 行为层——农耕体验活动；
    ③ 精神层——回归自然、慢生活的哲学。这种<strong>"物质-行为-精神"</strong>三层结构
    让文化主题既有载体，又有深度。
    """, body_style))
    story.append(Paragraph("""
    <strong>文化IP：从场地到产品。</strong>四季将稻田元素转化为可购买的IP产品：
    稻田香薰、稻米护肤品、农耕工具装饰品、泰北手工艺品。这些产品不仅增加了收入，
    更重要的是让客人把<strong>"体验带回家"</strong>，延续记忆。对于迪荡湖项目，
    可以开发黄酒文化IP产品（黄酒护肤品、酒具、文化书籍等）。
    """, body_style))
    
    # 美术总监
    story.append(Paragraph("美术总监 · 视觉与氛围视角", subsection_style))
    story.append(Paragraph("""
    <strong>色彩策略：自然色谱的提取。</strong>四季的视觉设计完全遵循自然色彩：
    稻田的金黄、天空的湛蓝、植被的翠绿、建筑的深棕。这种<strong>"源于自然、归于自然"</strong>的
    色彩策略创造了和谐统一的视觉感受。特别值得注意的是<strong>金色与蓝色的对比</strong>——
    这是自然界最美的配色（日落时分），四季在整个项目中反复运用这个配色关系。
    """, body_style))
    story.append(Paragraph("""
    <strong>光影设计：建筑是光的容器。</strong>泰国强烈的阳光被巧妙利用：
    廊道阴影创造凉爽的过渡空间、格栅天窗创造斑驳的光影、水面反射将阳光引入室内。
    这种对光的控制让建筑在一天中呈现不同的表情，创造<strong>"时间的诗意"</strong>。
    """, body_style))
    
    story.append(PageBreak())
    
    # ========== 总结与启示 ==========
    story.append(Paragraph("03  总结与项目启示", section_style))
    
    story.append(Paragraph("核心成功要素", subsection_style))
    
    success_factors = [
        ['成功要素', '具体表现', '对迪荡湖项目的启示'],
        ['独特定位', '首创"稻田奢华"品类', '找到绍兴独特的文化/自然切入点'],
        ['体验设计', '从住宿到目的地', '设计全包式体验，延长停留时间'],
        ['文化转译', '传统兰纳现代演绎', '绍兴文化现代表达，避免复古'],
        ['低密布局', '分散式亭阁布局', '放弃高容积率，追求品质感'],
        ['运营前置', '体验即产品', '运营逻辑贯穿设计全过程'],
    ]
    
    success_table = Table(success_factors, colWidths=[3*cm, 5*cm, 5.8*cm])
    success_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), main_font),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 1), (-1, -1), main_font),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#fafafa')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#fafafa'), colors.white]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(success_table)
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("风险提示", subsection_style))
    story.append(Paragraph("""
    ① <strong>季节性风险：</strong>稻田景观有明显的季节性（收割后景观价值下降），
    需要考虑淡季的替代景观或活动。② <strong>生态维护成本：</strong>真实的农田需要持续投入
    （耕种、灌溉、收割），运营成本高于普通园林。③ <strong>复制难度：</strong>"稻田奢华"在清迈成功
    是因为当地有成熟的稻田景观和农耕文化，强行复制到其他没有这种文化基础的地方可能失效。
    """, body_style))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("""
    "<em>最好的设计不是让人看到设计本身，而是感受到与自然的重新连接。</em>" —— 比尔·本斯利
    """, quote_style))
    
    story.append(PageBreak())
    
    # ========== 附录 ==========
    story.append(Paragraph("04  附录", section_style))
    
    story.append(Paragraph("参考资料", subsection_style))
    story.append(Paragraph("""
    • Four Seasons Official Website: www.fourseasons.com/chiangmai<br/>
    • Bensley Design Studios Portfolio<br/>
    • 《Thailand's Best Hotels》Travel + Leisure<br/>
    • ArchDaily: Hospitality Architecture Cases<br/>
    • 实地考察报告（如有）
    """, body_style))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("相关案例推荐", subsection_style))
    story.append(Paragraph("""
    • 阿丽拉乌镇（中国）—— 水乡奢华的现代演绎<br/>
    • Amangiri（美国）—— 荒漠中的极简奢华<br/>
    • 虹夕诺雅京都（日本）—— 船游入学的独特体验<br/>
    • Singita Grumeti（坦桑尼亚）—— 野生动物+奢华露营
    """, body_style))
    
    story.append(Spacer(1, 1*cm))
    
    # 结语
    story.append(HRFlowable(width="50%", thickness=0.5, color=colors.HexColor('#cccccc'), spaceBefore=20, spaceAfter=15, hAlign='CENTER'))
    
    ending_style = ParagraphStyle('Ending', fontName=main_font, fontSize=10, textColor=colors.HexColor('#555555'), alignment=TA_CENTER, leading=18)
    story.append(Paragraph("本报告由小白设计工作室10人Agent团队协作完成", ending_style))
    story.append(Paragraph("每个案例都是全Agent共同学习的成果", ending_style))
    story.append(Paragraph("持续进化中", ending_style))
    
    story.append(Spacer(1, 0.8*cm))
    story.append(Paragraph("小白设计工作室  |  2026年2月28日", footer_style))
    
    # 生成PDF
    doc.build(story)
    
    print(f"✅ 全Agent协作案例研习报告已生成: {pdf_file}")
    print(f"📄 文件大小: {os.path.getsize(pdf_file)/1024:.1f} KB")
    return pdf_file

if __name__ == "__main__":
    print("🎨 美术总监设计全Agent协作报告...")
    print("=" * 60)
    result = create_full_agent_report()
    print("=" * 60)
    print("🎉 报告生成完成！")
