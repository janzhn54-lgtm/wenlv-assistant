#!/usr/bin/env python3
"""
小白设计工作室 - 高质量案例分享报告 V2.0
美术总监主导设计，解决乱码问题，增加深度分享
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics import renderPDF
from datetime import datetime
import os

# 注册中文字体
def register_fonts():
    """注册中文字体"""
    fonts = [
        ('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 'WQYZenHei'),
        ('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 'WQYMicroHei'),
        ('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', 'NotoSansCJK'),
    ]
    
    registered = []
    for font_path, font_name in fonts:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont(font_name, font_path))
                registered.append(font_name)
                print(f"✅ 注册字体: {font_name}")
            except Exception as e:
                print(f"⚠️ 字体注册失败 {font_name}: {e}")
    
    return registered[0] if registered else 'Helvetica'

def create_case_report():
    """创建高质量案例分享报告"""
    
    # 注册字体
    main_font = register_fonts()
    print(f"使用主字体: {main_font}")
    
    today = datetime.now()
    
    # 创建PDF
    pdf_file = "reports/案例分享报告_高质量版.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=20*mm,
        leftMargin=20*mm,
        topMargin=20*mm,
        bottomMargin=20*mm
    )
    
    # 定义样式 - 美术总监设计
    styles = getSampleStyleSheet()
    
    # 主标题样式
    title_style = ParagraphStyle(
        'Title',
        fontName=main_font,
        fontSize=28,
        textColor=colors.HexColor('#1a1a2e'),
        spaceAfter=8,
        alignment=TA_CENTER,
        leading=36
    )
    
    # 副标题
    subtitle_style = ParagraphStyle(
        'Subtitle',
        fontName=main_font,
        fontSize=12,
        textColor=colors.HexColor('#666666'),
        spaceAfter=30,
        alignment=TA_CENTER,
        leading=16
    )
    
    # 章节标题
    section_style = ParagraphStyle(
        'Section',
        fontName=main_font,
        fontSize=16,
        textColor=colors.HexColor('#16213e'),
        spaceAfter=12,
        spaceBefore=20,
        leading=22,
        leftIndent=0
    )
    
    # 小标题
    subsection_style = ParagraphStyle(
        'Subsection',
        fontName=main_font,
        fontSize=13,
        textColor=colors.HexColor('#0f3460'),
        spaceAfter=8,
        spaceBefore=12,
        leading=18
    )
    
    # 正文
    body_style = ParagraphStyle(
        'Body',
        fontName=main_font,
        fontSize=10.5,
        textColor=colors.HexColor('#333333'),
        spaceAfter=8,
        leading=18,
        alignment=TA_JUSTIFY,
        firstLineIndent=24
    )
    
    # 重点文字
    highlight_style = ParagraphStyle(
        'Highlight',
        fontName=main_font,
        fontSize=11,
        textColor=colors.HexColor('#e94560'),
        spaceAfter=6,
        leading=16,
        leftIndent=12
    )
    
    # 引用样式
    quote_style = ParagraphStyle(
        'Quote',
        fontName=main_font,
        fontSize=10,
        textColor=colors.HexColor('#555555'),
        spaceAfter=12,
        leading=16,
        leftIndent=30,
        rightIndent=30,
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
    story.append(Spacer(1, 4*cm))
    
    # 装饰线
    story.append(HRFlowable(width="80%", thickness=2, color=colors.HexColor('#16213e'), spaceBefore=0, spaceAfter=20, hAlign='CENTER'))
    
    story.append(Paragraph("案例研习报告", title_style))
    story.append(Paragraph("Case Study Report · 深度分享", subtitle_style))
    
    story.append(HRFlowable(width="80%", thickness=2, color=colors.HexColor('#16213e'), spaceBefore=20, spaceAfter=40, hAlign='CENTER'))
    
    # 日期和编号
    date_style = ParagraphStyle('Date', fontName=main_font, fontSize=11, textColor=colors.HexColor('#666666'), alignment=TA_CENTER)
    story.append(Paragraph(f"{today.strftime('%Y年%m月%d日')}", date_style))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("第 001 期 · 全球文旅建筑精选", date_style))
    
    story.append(Spacer(1, 3*cm))
    
    # 工作室标识
    studio_style = ParagraphStyle('Studio', fontName=main_font, fontSize=14, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER)
    story.append(Paragraph("小白设计工作室", studio_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("10人专家团队 · 文旅专精 · 持续进化", subtitle_style))
    
    story.append(PageBreak())
    
    # ========== 本期导读 ==========
    story.append(Paragraph("本期导读", section_style))
    
    intro_text = """
    本期报告精选<strong>3个全球顶尖文旅建筑案例</strong>，涵盖精品酒店、文化建筑、度假综合体三种类型。
    通过对这些项目的深度剖析，我们希望为爸爸的项目提供<strong>可借鉴的设计策略、运营模式和文化表达方法</strong>。
    """
    story.append(Paragraph(intro_text, body_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 案例列表表格
    case_list_data = [
        ['序号', '案例名称', '地点', '类型', '核心亮点'],
        ['01', '清迈四季酒店', '泰国清迈', '精品度假酒店', '稻田景观×奢华体验'],
        ['02', '巴拉甘马术庄园', '墨西哥', '文化住宅', '空间诗学×情感唤醒'],
        ['03', '阿丽拉乌镇', '中国乌镇', '水乡度假酒店', '在地文化×现代极简'],
    ]
    
    case_table = Table(case_list_data, colWidths=[1.2*cm, 3.5*cm, 2.5*cm, 2.8*cm, 4*cm])
    case_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), main_font),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 1), (-1, -1), main_font),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8f9fa')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#f8f9fa'), colors.white]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(case_table)
    story.append(Spacer(1, 0.8*cm))
    
    story.append(Paragraph("学习重点", subsection_style))
    focus_points = [
        "• <strong>空间叙事</strong>：如何用建筑语言讲述文化故事",
        "• <strong>在地性表达</strong>：全球化语境下的本土文化转译",
        "• <strong>体验设计</strong>：从功能满足到情感共鸣的升级",
        "• <strong>运营逻辑</strong>：设计如何支撑商业可持续",
    ]
    for point in focus_points:
        story.append(Paragraph(point, body_style))
    
    story.append(PageBreak())
    
    # ========== 案例一 ==========
    story.append(Paragraph("案例一 · 清迈四季酒店", section_style))
    story.append(Paragraph("Four Seasons Resort Chiang Mai", subtitle_style))
    
    # 项目信息
    story.append(Paragraph("项目概况", subsection_style))
    
    info_data = [
        ['项目地点', '泰国，清迈府，湄林县'],
        ['开业时间', '1995年（2015年翻新）'],
        ['客房数量', '98间（64间亭阁+34间别墅）'],
        ['占地面积', '约12公顷'],
        ['设计团队', 'Bensley Design Studios'],
        ['参考房价', '¥3,500-8,000/晚'],
    ]
    
    info_table = Table(info_data, colWidths=[3*cm, 10*cm])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), main_font),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#0f3460')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#333333')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#eeeeee')),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.6*cm))
    
    # 核心亮点
    story.append(Paragraph("核心亮点", subsection_style))
    story.append(Paragraph("<strong>1. 稻田景观的极致演绎</strong>", highlight_style))
    story.append(Paragraph("""
    酒店最大的特色是将<strong>大片稻田</strong>融入度假村设计。客人在房间、餐厅、泳池都能俯瞰金黄稻田，
    参与插秧、收割等农事体验。这种"<strong>奢华酒店+田园生活</strong>"的组合创造了独特的差异化定位。
    """, body_style))
    
    story.append(Paragraph("<strong>2. 兰纳文化的现代表达</strong>", highlight_style))
    story.append(Paragraph("""
    建筑采用泰国北部兰纳王朝风格，坡屋顶、柚木材料、手工雕刻，但并非简单复制传统，
    而是通过<strong>简化线条、放大尺度、现代材料</strong>的混搭，让传统风格更符合当代审美。
    """, body_style))
    
    story.append(Paragraph("<strong>3. 私密性与开放性的平衡</strong>", highlight_style))
    story.append(Paragraph("""
    客房采用"<strong>分散式布局</strong>"，每间房都有独立景观和隐私空间；
    公共区域（餐厅、泳池）则强调开放性和社交性，形成"私享+共享"的层次。
    """, body_style))
    
    story.append(Spacer(1, 0.4*cm))
    
    # 深度分享
    story.append(Paragraph("研习分享 · 小白观点", subsection_style))
    story.append(Paragraph("""
    <strong>对爸爸项目的启示：</strong>
    """, body_style))
    story.append(Paragraph("""
    1. <strong>农业景观的价值被严重低估</strong>。在城市周边项目中，保留或引入农田、果园等农业元素，
    不仅成本低，还能创造独特的体验价值，形成"城市+田园"的差异化定位。
    """, body_style))
    story.append(Paragraph("""
    2. <strong>文化表达要"神似"而非"形似"</strong>。完全复制传统建筑会显得陈旧，
    关键是提炼文化精神（如兰纳的优雅、自然、手工艺），用现代手法重新演绎。
    """, body_style))
    story.append(Paragraph("""
    3. <strong>体验设计要"沉浸式"而非"观光式"</strong>。让客人参与插秧、烹饪、手工艺等活动，
    从旁观者变成参与者，大幅提升停留时间和满意度。
    """, body_style))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("""
    "<em>最好的奢华不是金碧辉煌，而是与自然和谐共处的能力。</em>" —— 比尔·本斯利
    """, quote_style))
    
    story.append(PageBreak())
    
    # ========== 案例二 ==========
    story.append(Paragraph("案例二 · 巴拉甘马术庄园", section_style))
    story.append(Paragraph("Cuadra San Cristóbal · Luis Barragán", subtitle_style))
    
    story.append(Paragraph("项目概况", subsection_style))
    
    info_data2 = [
        ['项目地点', '墨西哥，墨西哥州，阿蒂萨潘'],
        ['建造时间', '1966-1968年'],
        ['项目类型', '私人住宅/马术庄园'],
        ['建筑师', 'Luis Barragán（普利兹克奖得主）'],
        ['占地面积', '约4公顷'],
        ['现状', '世界文化遗产（2004年）'],
    ]
    
    info_table2 = Table(info_data2, colWidths=[3*cm, 10*cm])
    info_table2.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), main_font),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#0f3460')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#333333')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#eeeeee')),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(info_table2)
    story.append(Spacer(1, 0.6*cm))
    
    story.append(Paragraph("核心亮点", subsection_style))
    story.append(Paragraph("<strong>1. 色彩的情感力量</strong>", highlight_style))
    story.append(Paragraph("""
    巴拉甘大胆使用<strong>粉色墙体</strong>（墨西哥玫瑰色）与<strong>蓝色天空</strong>、<strong>绿色植物</strong>形成强烈对比。
    这种色彩组合不是装饰，而是<strong>情感触发器</strong>，让人感受到宁静、喜悦、神圣。
    """, body_style))
    
    story.append(Paragraph("<strong>2. 水面的空间魔法</strong>", highlight_style))
    story.append(Paragraph("""
    庄园中央的水池不仅是景观，更是<strong>空间倍增器</strong>。平静的水面反射天空和建筑，
    在视觉上将空间扩大一倍，同时带来清凉和宁静感。
    """, body_style))
    
    story.append(Paragraph("<strong>3. 尺度的戏剧化运用</strong>", highlight_style))
    story.append(Paragraph("""
    巴拉甘故意使用<strong>非人类尺度</strong>的墙体（4-5米高），让访客感到渺小，
    同时让马匹在其中显得协调。这种"<strong>以马为本</strong>"的尺度设计创造了独特的空间体验。
    """, body_style))
    
    story.append(Spacer(1, 0.4*cm))
    
    story.append(Paragraph("研习分享 · 小白观点", subsection_style))
    story.append(Paragraph("""
    <strong>对爸爸项目的启示：</strong>
    """, body_style))
    story.append(Paragraph("""
    1. <strong>色彩是最便宜却最有效的设计工具</strong>。不需要昂贵材料，
    一面纯色墙就能改变空间氛围。关键是选择与场地气质、文化背景契合的颜色。
    """, body_style))
    story.append(Paragraph("""
    2. <strong>水面是最好的"软装"</strong>。静态水面能反射、降温、增加湿度、扩大空间感，
    在文旅项目中，即使很小的水景也能大幅提升品质感。
    """, body_style))
    story.append(Paragraph("""
    3. <strong>"反常"的尺度创造记忆点</strong>。常规设计追求人体工学尺度，
    但偶尔打破常规（如超高的墙体、狭窄的通道）能创造戏剧性和记忆点。
    """, body_style))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("""
    "<em>建筑应该唤醒情感，而不只是提供功能。</em>" —— 路易斯·巴拉甘
    """, quote_style))
    
    story.append(PageBreak())
    
    # ========== 案例三 ==========
    story.append(Paragraph("案例三 · 阿丽拉乌镇", section_style))
    story.append(Paragraph("Alila Wuzhen · 中国水乡新演绎", subtitle_style))
    
    story.append(Paragraph("项目概况", subsection_style))
    
    info_data3 = [
        ['项目地点', '中国，浙江，桐乡，乌镇'],
        ['开业时间', '2018年'],
        ['客房数量', '125间'],
        ['建筑设计', 'GOA大象设计'],
        ['室内设计', '水平线设计'],
        ['占地面积', '约2.5公顷'],
    ]
    
    info_table3 = Table(info_data3, colWidths=[3*cm, 10*cm])
    info_table3.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), main_font),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#0f3460')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#333333')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#eeeeee')),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(info_table3)
    story.append(Spacer(1, 0.6*cm))
    
    story.append(Paragraph("核心亮点", subsection_style))
    story.append(Paragraph('<strong>1. "抽象水乡"的空间策略</strong>', highlight_style))
    story.append(Paragraph("""
    没有直接复制传统江南建筑，而是<strong>抽象提炼</strong>：白墙、黑瓦、水院被简化为几何体块，
    用现代极简语言重新演绎水乡意境，既有<strong>文化识别性</strong>，又有<strong>当代感</strong>。
    """, body_style))
    
    story.append(Paragraph("<strong>2. 内向型院落布局</strong>", highlight_style))
    story.append(Paragraph("""
    不同于西栅的街道导向，阿丽拉采用<strong>内向型院落</strong>。从外面看是简洁的白墙，
    内部却是层次丰富的水院、天井、回廊，形成"<strong>外简内繁</strong>"的对比。
    """, body_style))
    
    story.append(Paragraph("<strong>3. 光影的诗意运用</strong>", highlight_style))
    story.append(Paragraph("""
    设计师精确计算<strong>光线角度</strong>，在不同时间创造不同的光影效果。
    早晨的阳光透过格栅洒在地面，傍晚的余晖映照在白墙上，建筑成为<strong>光的容器</strong>。
    """, body_style))
    
    story.append(Spacer(1, 0.4*cm))
    
    story.append(Paragraph("研习分享 · 小白观点", subsection_style))
    story.append(Paragraph("""
    <strong>对爸爸项目的启示：</strong>
    """, body_style))
    story.append(Paragraph("""
    1. <strong>"神似"优于"形似"</strong>。在文化项目中，不需要完全复制传统建筑，
    关键是抓住文化精神（水乡的留白、流动、意境），用现代手法转译。
    """, body_style))
    story.append(Paragraph("""
    2. <strong>内向型布局的隐私优势</strong>。对于高端酒店/住宅，
    内向型院落比街道导向更能保证隐私，同时创造独享的景观资源。
    """, body_style))
    story.append(Paragraph("""
    3. <strong>光影是最精致的设计</strong>。在中国文化语境中，
    光影变化本身就是景观（如苏州园林的"移步换景"），设计中要充分考虑光的运用。
    """, body_style))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("""
    "<em>好的设计不是让人看到设计本身，而是感受到空间的诗意。</em>" —— 琚宾（水平线设计）
    """, quote_style))
    
    story.append(PageBreak())
    
    # ========== 总结 ==========
    story.append(Paragraph("总结与启示", section_style))
    
    story.append(Paragraph("三个案例的共同规律", subsection_style))
    
    summary_points = [
        "1. <strong>文化不是装饰，而是灵魂</strong>：三个项目都深入挖掘在地文化，但不是简单复制，而是提炼精神内核后用现代手法转译。",
        "2. <strong>自然是最佳合作伙伴</strong>：稻田、水面、光影，这些自然元素被巧妙运用，创造低成本高价值的体验。",
        "3. <strong>体验重于形式</strong>：设计不只是看起来美，更要让人<strong>感受到什么</strong>——宁静、喜悦、诗意。",
        '4. <strong>差异化来自独特视角</strong>：四季的"田园奢华"、巴拉甘的"以马为本"、阿丽拉的"抽象水乡"，都是从独特视角切入，避免同质化。',
    ]
    
    for point in summary_points:
        story.append(Paragraph(point, body_style))
        story.append(Spacer(1, 0.2*cm))
    
    story.append(Spacer(1, 0.4*cm))
    
    story.append(Paragraph("对迪荡湖项目的具体建议", subsection_style))
    
    suggestions = [
        '• <strong>文化定位</strong>：挖掘绍兴"胆剑精神"、黄酒文化、名士文化，找到独特的文化切入点。',
        '• <strong>空间策略</strong>：参考阿丽拉的"抽象水乡"，用现代极简语言演绎江南意境，而非简单复制传统。',
        '• <strong>体验设计</strong>：借鉴四季的"沉浸式体验"，设计黄酒酿造体验、书法体验、乌篷船夜游等活动。',
        '• <strong>景观策略</strong>：学习巴拉甘的色彩和水面运用，用粉墙黛瓦+水面倒影创造诗意空间。',
    ]
    
    for suggestion in suggestions:
        story.append(Paragraph(suggestion, body_style))
        story.append(Spacer(1, 0.15*cm))
    
    story.append(Spacer(1, 0.8*cm))
    
    # 结语
    story.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor('#cccccc'), spaceBefore=20, spaceAfter=20, hAlign='CENTER'))
    
    ending_style = ParagraphStyle('Ending', fontName=main_font, fontSize=11, textColor=colors.HexColor('#555555'), alignment=TA_CENTER, leading=20)
    story.append(Paragraph("案例研习是一个持续的过程", ending_style))
    story.append(Paragraph("我们将继续深入研究全球优秀项目", ending_style))
    story.append(Paragraph("为爸爸的项目提供最有价值的参考", ending_style))
    
    story.append(Spacer(1, 0.8*cm))
    
    story.append(Paragraph("小白设计工作室", footer_style))
    story.append(Paragraph("2026年2月28日", footer_style))
    
    # 生成PDF
    doc.build(story)
    
    print(f"✅ 高质量案例分享报告已生成: {pdf_file}")
    print(f"📄 文件大小: {os.path.getsize(pdf_file)/1024:.1f} KB")
    return pdf_file

if __name__ == "__main__":
    print("🎨 美术总监正在设计高质量案例分享报告...")
    print("=" * 50)
    result = create_case_report()
    print("=" * 50)
    print("🎉 报告生成完成！")
