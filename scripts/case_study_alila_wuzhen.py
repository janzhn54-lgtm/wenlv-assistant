#!/usr/bin/env python3
"""
小白设计工作室 - 全Agent协作案例研习报告 V3.0
案例二：阿丽拉乌镇
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

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

def create_report():
    main_font = register_fonts()
    today = datetime.now()
    pdf_file = "reports/案例研习报告_阿丽拉乌镇_全Agent协作版.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=15*mm, leftMargin=15*mm, topMargin=15*mm, bottomMargin=15*mm)
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('Title', fontName=main_font, fontSize=26, textColor=colors.HexColor('#1a1a2e'), spaceAfter=6, alignment=TA_CENTER, leading=32)
    subtitle_en_style = ParagraphStyle('SubtitleEn', fontName='Helvetica', fontSize=11, textColor=colors.HexColor('#666666'), spaceAfter=20, alignment=TA_CENTER, leading=14)
    section_style = ParagraphStyle('Section', fontName=main_font, fontSize=15, textColor=colors.HexColor('#16213e'), spaceAfter=10, spaceBefore=16, leading=20)
    subsection_style = ParagraphStyle('Subsection', fontName=main_font, fontSize=12, textColor=colors.HexColor('#0f3460'), spaceAfter=6, spaceBefore=10, leading=16)
    body_style = ParagraphStyle('Body', fontName=main_font, fontSize=9.5, textColor=colors.HexColor('#333333'), spaceAfter=5, leading=15, alignment=TA_JUSTIFY, firstLineIndent=20)
    quote_style = ParagraphStyle('Quote', fontName=main_font, fontSize=9, textColor=colors.HexColor('#555555'), spaceAfter=8, leading=14, leftIndent=25, rightIndent=25, fontStyle='italic')
    footer_style = ParagraphStyle('Footer', fontName=main_font, fontSize=8, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, leading=12)
    
    story = []
    
    # 封面
    story.append(Spacer(1, 3.5*cm))
    story.append(HRFlowable(width="70%", thickness=2, color=colors.HexColor('#16213e'), spaceBefore=0, spaceAfter=15, hAlign='CENTER'))
    story.append(Paragraph("全Agent协作 · 案例研习报告", title_style))
    story.append(Paragraph("Multi-Agent Collaborative Case Study Report", subtitle_en_style))
    story.append(HRFlowable(width="70%", thickness=2, color=colors.HexColor('#16213e'), spaceBefore=15, spaceAfter=25, hAlign='CENTER'))
    
    case_name_style = ParagraphStyle('CaseName', fontName=main_font, fontSize=18, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER, spaceAfter=8)
    story.append(Paragraph("阿丽拉乌镇", case_name_style))
    story.append(Paragraph("Alila Wuzhen · 中国水乡新演绎", subtitle_en_style))
    
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("参与分析 Agent 团队", ParagraphStyle('TeamTitle', fontName=main_font, fontSize=10, textColor=colors.HexColor('#666666'), alignment=TA_CENTER, spaceAfter=10)))
    
    agent_tags = [['规划法规', '城市设计', '建筑设计', '投资金融'], ['文旅运营', '文化策划', '美术总监', '文字工作者']]
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
    date_style = ParagraphStyle('Date', fontName=main_font, fontSize=10, textColor=colors.HexColor('#666666'), alignment=TA_CENTER)
    story.append(Paragraph(f"{today.strftime('%Y年%m月%d日')}  |  第002期", date_style))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("小白设计工作室", ParagraphStyle('Studio', fontName=main_font, fontSize=12, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER)))
    story.append(Paragraph("10人专家团队 · 深度协作分析 · 持续进化", subtitle_en_style))
    
    story.append(PageBreak())
    
    # 项目概况
    story.append(Paragraph("01  项目概况", section_style))
    
    info_data = [
        ['项目名称', '阿丽拉乌镇酒店 (Alila Wuzhen)'],
        ['项目地点', '中国浙江省桐乡市乌镇镇，紧邻西栅景区'],
        ['开业时间', '2018年'],
        ['客房规模', '125间（水舍、云舍、花园别墅）'],
        ['占地面积', '约2.5公顷'],
        ['建筑面积', '约2.8万平方米'],
        ['建筑设计', 'GOA大象设计（浙江）'],
        ['室内设计', '水平线设计（琚宾）'],
        ['景观设计', 'ZSD卓时设计'],
        ['投资规模', '约5亿人民币'],
        ['参考房价', '¥2,500-6,000/晚'],
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
    阿丽拉乌镇是<strong>中国本土设计力量</strong>打造的国际级奢华度假酒店典范。
    项目摒弃了传统仿古建筑的套路，开创了<strong>"抽象水乡"</strong>的全新设计语汇——
    用现代极简主义重新演绎江南文化，被誉为<strong>"最美阿丽拉"</strong>。
    酒店不是简单的住宿设施，而是一个让人重新理解江南、体验当代东方美学的文化容器。
    """, body_style))
    
    story.append(PageBreak())
    
    # Agent协作分析
    story.append(Paragraph("02  Agent协作深度分析", section_style))
    
    # 规划法规专家
    story.append(Paragraph("规划法规专家 · 合规与政策视角", subsection_style))
    story.append(Paragraph("""
    <strong>用地性质与规划指标：</strong>阿丽拉乌镇位于乌镇镇区边缘，用地性质为商业服务业设施用地（旅馆用地）。
    规划指标控制严格：容积率约1.1，建筑密度约35%，绿地率约30%，建筑高度控制在3层（约15米）以内。
    这些指标对建筑设计形成了刚性约束，但也倒逼出<strong>"内向型院落"</strong>的创新布局。
    对于迪荡湖项目，需要提前确认<strong>滨水建筑退界要求</strong>和<strong>高度控制</strong>，避免方案反复。
    """, body_style))
    story.append(Paragraph("""
    <strong>风貌协调与审批路径：</strong>乌镇作为世界文化遗产地，对建筑风貌有严格控制。
    阿丽拉的"抽象水乡"策略正是在这种约束下的创新——既满足了风貌协调要求（白墙黛瓦的整体色调），
    又避免了仿古建筑的低俗。审批过程中，设计方案经过了多轮专家论证，最终获得通过。
    这说明在保护区内，<strong>创新而非复古</strong>是可以被接受的，关键是要有文化深度。
    """, body_style))
    
    # 城市设计专家
    story.append(Paragraph("城市设计专家 · 空间规划视角", subsection_style))
    story.append(Paragraph("""
    <strong>空间结构："内向型院落"系统。</strong>阿丽拉最大的创新是摒弃了传统水乡"街道导向"的布局，
    采用<strong>内向型院落</strong>。从外面看，酒店是一圈简洁的白墙，与乌镇传统民居尺度协调；
    进入内部，却是层次丰富的水院、天井、回廊。这种<strong>"外简内繁"</strong>的策略创造了三重价值：
    ① 保证客人隐私，避免游客窥探；② 创造独享的景观资源；③ 建筑与外部街道尺度协调。
    """, body_style))
    story.append(Paragraph("""
    <strong>空间序列：从"压迫"到"释放"。</strong>酒店精心设计了空间节奏：入口巷道（窄、暗、压迫）→
    接待门厅（过渡）→ 中央水院（展开、明亮）。这种<strong>先抑后扬</strong>的手法，
    让客人在进入客房前经历情绪的起伏，最终在水院达到高潮。对于类似项目，
    <strong>空间序列的设计比单栋建筑更重要</strong>，它决定了客人的第一印象和情感体验。
    """, body_style))
    
    # 建筑设计专家
    story.append(Paragraph("建筑设计专家 · 建筑与美学视角", subsection_style))
    story.append(Paragraph("""
    <strong>建筑语言：极简主义的江南转译。</strong>阿丽拉没有使用传统建筑的飞檐翘角、雕花门窗，
    而是提炼了江南建筑的<strong>本质特征</strong>：白墙、黛瓦、水院、天井，用现代极简语言重新演绎。
    建筑体量由简单的立方体、长方体构成，墙面是纯粹的白，屋顶是纯粹的深灰。
    这种"少即是多"的处理，让建筑既有<strong>文化识别性</strong>（一看就是江南），
    又有<strong>当代性</strong>（不仿古、不陈旧）。
    """, body_style))
    story.append(Paragraph("""
    <strong>材料策略：当代材料的东方气质。</strong>建筑使用了大量当代材料：白色涂料、深灰色铝板、
    超白玻璃、清水混凝土。但这些材料通过精心处理，呈现出东方气质：
    白色涂料的哑光质感像宣纸，深灰铝板的纹理像瓦片，超白玻璃的反射像水面。
    这种<strong>"新瓶装旧酒"</strong>的材料策略，既保证了建造质量和耐久性，又创造了文化意境。
    """, body_style))
    
    story.append(PageBreak())
    
    # 投资金融专家
    story.append(Paragraph("投资金融专家 · 投资与收益视角", subsection_style))
    story.append(Paragraph("""
    <strong>投资结构：中等规模，精品定位。</strong>阿丽拉乌镇总投资约5亿人民币，125间客房，
    单房投资约400万元。这个投资强度在国内精品酒店中属于<strong>中高水平</strong>，
    体现了"少而精"的定位策略。与四季清迈的"重资产长回收期"模式不同，
    阿丽拉的规模更适合<strong>快速验证市场</strong>和调整运营策略。
    """, body_style))
    story.append(Paragraph("""
    <strong>收益模型：ADR×OCC+二次消费。</strong>阿丽拉的ADR约¥3,500，OCC约60-70%，RevPAR约¥2,100。
    二次消费（餐饮、SPA、活动）占比约35%，低于四季清迈的40%，
    说明阿丽拉还在<strong>提升运营能力</strong>的过程中。关键启示：
    ① 开业初期OCC通常较低，需要2-3年培育期；② 二次消费需要持续的产品创新；
    ③ 地理位置（紧邻西栅）是重要优势，但也意味着需要与景区差异化竞争。
    """, body_style))
    story.append(Paragraph("""
    <strong>品牌溢价：本土设计的力量。</strong>阿丽拉乌镇的成功证明，<strong>本土设计团队</strong>（GOA大象设计、
    水平线设计）完全有能力打造国际级项目。相比聘请国外设计师，本土团队更了解文化、
    更易沟通、成本更低。对于迪荡湖项目，建议优先考虑<strong>浙江本土优秀设计团队</strong>。
    """, body_style))
    
    # 文旅运营专家
    story.append(Paragraph("文旅运营专家 · 运营与体验视角", subsection_style))
    story.append(Paragraph("""
    <strong>运营定位：从"酒店"到"目的地"。</strong>阿丽拉不仅是住宿设施，更是一个让人<strong>"住在乌镇外、体验乌镇魂"</strong>
    的文化场所。酒店提供多种文化活动：清晨水巷漫步、午后茶艺体验、傍晚评弹欣赏、夜间灯笼夜游。
    这些活动让客人即使不进入西栅景区，也能深度体验乌镇文化。
    """, body_style))
    story.append(Paragraph("""
    <strong>竞争策略：与景区的差异化定位。</strong>西栅的问题是游客太多、太嘈杂。阿丽拉的定位是<strong>"私密、安静、当代"</strong>——
    与西栅的"热闹、传统、公共"形成对比。这种差异化让阿丽拉吸引了<strong>高端客群</strong>：
    商务人士、情侣度假、小型家庭聚会。对于迪荡湖项目，需要明确与周边竞品的<strong>差异化定位</strong>，
    不能简单复制现有模式。
    """, body_style))
    story.append(Paragraph("""
    <strong>服务创新：管家式服务。</strong>阿丽拉提供一对一管家服务，从预订到离店全程跟进。
    管家不仅提供服务，更担任<strong>文化向导</strong>角色，为客人讲解乌镇历史、推荐小众景点。
    这种服务增加了人力成本，但大幅提升了<strong>客人满意度和复购率</strong>。
    """, body_style))
    
    story.append(PageBreak())
    
    # 文化策划专家
    story.append(Paragraph("文化策划专家 · 文化与IP视角", subsection_style))
    story.append(Paragraph("""
    <strong>文化主题："抽象水乡"。</strong>阿丽拉的文化定位非常精准：不是"住在古镇里"，
    而是<strong>"住在当代对水乡的想象中"</strong>。这个主题有几个层次：
    ① 视觉层——白墙黛瓦的抽象；② 空间层——水院天井的意境；
    ③ 精神层——江南文化的当代转译。这种<strong>"抽象而非具象"</strong>的文化策略，
    让项目既有文化深度，又避免了仿古建筑的庸俗。
    """, body_style))
    story.append(Paragraph("""
    <strong>文化体验：从"看"到"感"。</strong>阿丽拉不提供"参观式"的文化体验（如博物馆），
    而是提供<strong>"沉浸式"体验</strong>：住在水院里、走在石板路上、看着天井的天空——
    文化成为生活方式的一部分。这种"润物细无声"的文化表达，比说教式的展示更有效。
    """, body_style))
    
    # 美术总监
    story.append(Paragraph("美术总监 · 视觉与氛围视角", subsection_style))
    story.append(Paragraph("""
    <strong>色彩策略：纯粹的二元对比。</strong>阿丽拉的视觉设计极其克制：只有白（墙）和深灰（顶）两种主色，
    点缀以木色（门窗）和绿色（植物）。这种<strong>极简的色彩策略</strong>创造了强烈的视觉识别性。
    值得注意的是，白色不是纯白，而是带一点点暖，在江南阴天的光线下显得温润；
    深灰不是黑，而是带一点点蓝，倒映在水中有墨色的质感。
    """, body_style))
    story.append(Paragraph("""
    <strong>光影设计：天井的诗学。</strong>阿丽拉大量运用天井和水面，创造了丰富的光影变化：
    天井将天空引入室内、水面反射阳光到墙面、格栅创造斑驳的阴影。
    这种对光的控制，让建筑在一天中呈现不同的<strong>"表情"</strong>，创造了时间的诗意。
    """, body_style))
    
    story.append(PageBreak())
    
    # 总结与启示
    story.append(Paragraph("03  总结与项目启示", section_style))
    
    story.append(Paragraph("核心成功要素", subsection_style))
    
    success_factors = [
        ['成功要素', '具体表现', '对迪荡湖项目的启示'],
        ['文化转译', '抽象水乡而非仿古', '绍兴文化现代表达，避免复古复制'],
        ['内向布局', '外简内繁的院落', '保证隐私，创造独享景观'],
        ['本土设计', 'GOA+水平线组合', '优先选择浙江本土优秀团队'],
        ['空间序列', '先抑后扬的节奏', '重视空间体验，不只建筑造型'],
        ['材料创新', '当代材料的东方感', '新材料+传统工艺的结合'],
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
    ① <strong>运营培育期长：</strong>阿丽拉开业初期OCC较低，需要2-3年市场培育，
    前期可能面临亏损压力。② <strong>与景区的竞合关系：</strong>紧邻景区既是优势也是挑战，
    需要明确差异化定位，避免被景区"淹没"。③ <strong>设计落地难度：</strong>极简设计对施工精度要求极高，
    白色墙面、清水混凝土等工艺需要高水平施工团队。
    """, body_style))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("""
    "<em>传统不是模仿，而是精神的延续。</em>" —— 琚宾（水平线设计）
    """, quote_style))
    
    story.append(PageBreak())
    
    # 附录
    story.append(Paragraph("04  附录", section_style))
    
    story.append(Paragraph("参考资料", subsection_style))
    story.append(Paragraph("""
    • GOA大象设计官网：www.goa.com.cn<br/>
    • 水平线设计官网：www.hsdesign.com.cn<br/>
    • ArchDaily: Alila Wuzhen项目页<br/>
    • 《琚宾作品集》<br/>
    • 实地考察报告（如有）
    """, body_style))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("相关案例推荐", subsection_style))
    story.append(Paragraph("""
    • 宁波柏悦酒店（中国）—— 宁波本土文化的现代表达<br/>
    • 苏州托尼洛·兰博基尼书苑酒店（中国）—— 园林意境的当代演绎<br/>
    • 京都安缦（日本）—— 极简主义与传统建筑的融合<br/>
    • 上海养云安缦（中国）—— 古建保护与现代功能的结合
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
    
    doc.build(story)
    
    print(f"✅ 阿丽拉乌镇全Agent协作报告已生成: {pdf_file}")
    print(f"📄 文件大小: {os.path.getsize(pdf_file)/1024:.1f} KB")
    return pdf_file

if __name__ == "__main__":
    print("🎨 生成阿丽拉乌镇全Agent协作报告...")
    print("=" * 60)
    result = create_report()
    print("=" * 60)
    print("🎉 报告生成完成！")
