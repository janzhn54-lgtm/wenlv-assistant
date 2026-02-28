#!/usr/bin/env python3
"""
小白设计工作室 - 案例研习报告 V4.0
优化排版、移除项目建议、增加图文丰富度
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
    pdf_file = "reports/案例研习报告_V4_优化版.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=15*mm, leftMargin=15*mm, topMargin=15*mm, bottomMargin=15*mm)
    
    # 样式定义 - 优化对齐
    title_style = ParagraphStyle('Title', fontName=main_font, fontSize=24, textColor=colors.HexColor('#1a1a2e'), spaceAfter=8, alignment=TA_CENTER, leading=30)
    subtitle_style = ParagraphStyle('Subtitle', fontName=main_font, fontSize=11, textColor=colors.HexColor('#666666'), spaceAfter=20, alignment=TA_CENTER, leading=14)
    section_style = ParagraphStyle('Section', fontName=main_font, fontSize=14, textColor=colors.HexColor('#16213e'), spaceAfter=10, spaceBefore=14, leading=18)
    subsection_style = ParagraphStyle('Subsection', fontName=main_font, fontSize=11, textColor=colors.HexColor('#0f3460'), spaceAfter=6, spaceBefore=10, leading=15)
    
    # 正文样式 - 优化对齐，避免空格问题
    body_style = ParagraphStyle(
        'Body',
        fontName=main_font,
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        spaceAfter=6,
        leading=14,
        alignment=TA_LEFT,  # 改为左对齐，避免两端对齐导致的空格问题
        firstLineIndent=18,
        wordWrap='CJK',  # 中文换行优化
    )
    
    quote_style = ParagraphStyle('Quote', fontName=main_font, fontSize=9, textColor=colors.HexColor('#555555'), spaceAfter=8, leading=14, leftIndent=20, rightIndent=20, fontStyle='italic')
    footer_style = ParagraphStyle('Footer', fontName=main_font, fontSize=8, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, leading=12)
    
    story = []
    
    # 封面
    story.append(Spacer(1, 4*cm))
    story.append(HRFlowable(width="60%", thickness=1.5, color=colors.HexColor('#16213e'), spaceBefore=0, spaceAfter=12, hAlign='CENTER'))
    story.append(Paragraph("案例研习报告", title_style))
    story.append(Paragraph("Case Study Report · Volume 001", subtitle_style))
    story.append(HRFlowable(width="60%", thickness=1.5, color=colors.HexColor('#16213e'), spaceBefore=12, spaceAfter=20, hAlign='CENTER'))
    
    story.append(Paragraph("清迈四季度假酒店", ParagraphStyle('CaseTitle', fontName=main_font, fontSize=16, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER, spaceAfter=6)))
    story.append(Paragraph("Four Seasons Resort Chiang Mai, Thailand", subtitle_style))
    
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("10-Agent Collaborative Analysis", subtitle_style))
    
    agent_box = [
        ['规划法规', '城市设计', '建筑设计', '投资金融'],
        ['文旅运营', '文化策划', '美术总监', '文字工作者']
    ]
    agent_table = Table(agent_box, colWidths=[2.8*cm]*4, rowHeights=[0.7*cm]*2)
    agent_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('FONTNAME', (0,0), (-1,-1), main_font),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(agent_table)
    
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph(f"{today.strftime('%Y年%m月%d日')}", subtitle_style))
    story.append(Paragraph("小白设计工作室", ParagraphStyle('Studio', fontName=main_font, fontSize=12, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER)))
    
    story.append(PageBreak())
    
    # 项目概况
    story.append(Paragraph("01 项目概况", section_style))
    
    # 项目信息表格 - 优化对齐
    info_data = [
        ['项目名称', '清迈四季度假酒店'],
        ['英文名称', 'Four Seasons Resort Chiang Mai'],
        ['项目地点', '泰国清迈府湄林县'],
        ['开业时间', '1995年（2015年翻新）'],
        ['客房数量', '98间（64间亭阁套房+34间别墅）'],
        ['占地面积', '约12公顷'],
        ['设计团队', 'Bensley Design Studios'],
        ['业主', '泰国本地财团（四季集团管理）'],
        ['参考房价', 'USD 500-1,200/晚'],
    ]
    
    info_table = Table(info_data, colWidths=[2.5*cm, 11.3*cm])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), main_font),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TEXTCOLOR', (0,0), (0,-1), colors.HexColor('#0f3460')),
        ('TEXTCOLOR', (1,0), (1,-1), colors.HexColor('#333333')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0e0e0')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f5f5f5')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.4*cm))
    
    # 图片占位说明
    story.append(Paragraph("【项目实景照片区域】", ParagraphStyle('ImageNote', fontName=main_font, fontSize=9, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceAfter=6)))
    story.append(Paragraph("注：此处应插入项目实景照片，包括稻田景观、建筑外观、客房实景等", body_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("项目简介", subsection_style))
    story.append(Paragraph("""
    清迈四季是全球公认的稻田奢华度假酒店典范。项目将大片农田融入高端度假体验，
    开创了农业景观与奢华服务结合的全新品类。酒店不仅提供住宿，更是一个让人重新连接自然、
    体验乡村生活的文化场所。
    """, body_style))
    
    story.append(PageBreak())
    
    # Agent分析部分
    story.append(Paragraph("02 Agent协作分析", section_style))
    
    # 城市设计专家 - 加入规划图说明
    story.append(Paragraph("城市设计专家", subsection_style))
    story.append(Paragraph("""
    空间布局采用散点式亭阁系统。64间亭阁如散落的珍珠分布在稻田中，
    通过蜿蜒的步道和电瓶车路网连接。这种布局创造三重价值：
    每间房都有独立稻田景观；保证客人隐私；减少建筑对农田的视觉冲击。
    """, body_style))
    
    story.append(Paragraph("【规划平面图区域】", ParagraphStyle('ImageNote', fontName=main_font, fontSize=9, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("注：此处应插入总平面图，展示建筑布局与稻田关系", body_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 建筑设计专家
    story.append(Paragraph("建筑设计专家", subsection_style))
    story.append(Paragraph("""
    建筑采用泰国北部兰纳王朝风格，特征为陡峭的多层坡屋顶、深色柚木材料、精美的木雕装饰。
    设计师比尔本斯利进行了现代简化：屋顶比例更修长、装饰更克制、空间更开敞。
    这种神似而非形似的处理让建筑既有文化识别性，又不显陈旧。
    """, body_style))
    
    story.append(Paragraph("【建筑立面图区域】", ParagraphStyle('ImageNote', fontName=main_font, fontSize=9, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("注：此处应插入建筑立面图和剖面图", body_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 投资金融专家 - 加入数据表格
    story.append(Paragraph("投资金融专家", subsection_style))
    story.append(Paragraph("""
    四季酒店开业投资约8000万美元。这种重资产模式依赖长期持有和运营增值。
    收益模型中，ADR约USD 400-500，OCC约65-75%，RevPAR约USD 280。
    二次消费（餐饮、SPA、体验活动）收入占比约40%，这部分利润率高于房费。
    """, body_style))
    
    # 经济数据表格
    story.append(Paragraph("财务指标参考", ParagraphStyle('TableTitle', fontName=main_font, fontSize=9, textColor=colors.HexColor('#0f3460'), spaceBefore=6, spaceAfter=4)))
    
    finance_data = [
        ['指标', '数值', '说明'],
        ['开业投资', '约8000万美元', '1995年'],
        ['客房数', '98间', '64亭阁+34别墅'],
        ['ADR', 'USD 400-500', '日均房价'],
        ['OCC', '65-75%', '入住率'],
        ['RevPAR', 'USD 280', '每间可售房收入'],
        ['二次消费占比', '40%', '餐饮、SPA、活动'],
    ]
    
    finance_table = Table(finance_data, colWidths=[3*cm, 3*cm, 7.8*cm])
    finance_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), main_font),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
        ('FONTNAME', (0,1), (-1,-1), main_font),
        ('FONTSIZE', (0,1), (-1,-1), 8.5),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(finance_table)
    story.append(Spacer(1, 0.4*cm))
    
    story.append(PageBreak())
    
    # 文旅运营专家 - 加入运营表格
    story.append(Paragraph("文旅运营专家", subsection_style))
    story.append(Paragraph("""
    四季的成功在于它不仅仅是一家酒店，而是一个旅游目的地。
    客人可以不离开酒店就度过3-5天：早晨稻田瑜伽、上午插秧体验、下午水疗SPA、
    傍晚稻田晚餐、夜间星空观星。这种全包式体验大幅延长了客人停留时间。
    """, body_style))
    
    # 运营活动表格
    story.append(Paragraph("体验活动安排示例", ParagraphStyle('TableTitle', fontName=main_font, fontSize=9, textColor=colors.HexColor('#0f3460'), spaceBefore=6, spaceAfter=4)))
    
    activity_data = [
        ['时段', '活动', '类型'],
        ['06:00-08:00', '稻田瑜伽', '康体'],
        ['09:00-11:00', '插秧体验', '农耕'],
        ['14:00-16:00', '水疗SPA', '休闲'],
        ['17:00-19:00', '泰餐烹饪课', '文化'],
        ['19:00-21:00', '稻田晚餐', '餐饮'],
    ]
    
    activity_table = Table(activity_data, colWidths=[3*cm, 5*cm, 5.8*cm])
    activity_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f3460')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), main_font),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
        ('FONTNAME', (0,1), (-1,-1), main_font),
        ('FONTSIZE', (0,1), (-1,-1), 8.5),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(activity_table)
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("【运营场景照片区域】", ParagraphStyle('ImageNote', fontName=main_font, fontSize=9, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("注：此处应插入活动场景照片、餐饮照片、SPA照片等", body_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 文化策划专家
    story.append(Paragraph("文化策划专家", subsection_style))
    story.append(Paragraph("""
    四季的文化定位精准：稻田里的奢华。这个主题有几个层次：
    物质层是真实的稻田景观；行为层是农耕体验活动；
    精神层是回归自然、慢生活的哲学。这种三层结构让文化主题既有载体又有深度。
    """, body_style))
    
    # 美术总监
    story.append(Paragraph("美术总监", subsection_style))
    story.append(Paragraph("""
    四季的视觉设计完全遵循自然色彩：稻田的金黄、天空的湛蓝、植被的翠绿、建筑的深棕。
    这种源于自然归于自然的色彩策略创造了和谐统一的视觉感受。
    金色与蓝色的对比是自然界最美的配色，四季在整个项目中反复运用。
    """, body_style))
    
    story.append(PageBreak())
    
    # 总结
    story.append(Paragraph("03 总结", section_style))
    
    story.append(Paragraph("核心学习要点", subsection_style))
    
    summary_points = [
        ['维度', '关键学习点'],
        ['空间规划', '散点式布局创造私密性和景观独占性'],
        ['建筑设计', '传统文化现代转译，神似而非形似'],
        ['投资模式', '重资产长周期，二次消费提升收益'],
        ['运营策略', '从住宿到目的地，全包式体验设计'],
        ['文化表达', '物质-行为-精神三层文化结构'],
        ['视觉设计', '源于自然的色彩策略'],
    ]
    
    summary_table = Table(summary_points, colWidths=[3*cm, 10.8*cm])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), main_font),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
        ('FONTNAME', (0,1), (-1,-1), main_font),
        ('FONTSIZE', (0,1), (-1,-1), 8.5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("""
    最好的设计不是让人看到设计本身，而是感受到与自然的重新连接。
    """, quote_style))
    
    story.append(Spacer(1, 0.5*cm))
    
    # 附录
    story.append(Paragraph("04 附录", section_style))
    story.append(Paragraph("参考资料", subsection_style))
    story.append(Paragraph("""
    • Four Seasons Official Website
    • Bensley Design Studios Portfolio
    • ArchDaily Hospitality Architecture
    • Travel + Leisure Hotel Reviews
    """, body_style))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("相关案例推荐", subsection_style))
    story.append(Paragraph("""
    • 阿丽拉乌镇（中国）—— 抽象水乡的现代演绎
    • Amangiri（美国）—— 荒漠中的极简奢华
    • 虹夕诺雅京都（日本）—— 船游入学的独特体验
    """, body_style))
    
    story.append(Spacer(1, 1*cm))
    
    # 结语
    story.append(HRFlowable(width="40%", thickness=0.5, color=colors.HexColor('#cccccc'), spaceBefore=15, spaceAfter=10, hAlign='CENTER'))
    story.append(Paragraph("本报告为学习研究用途", footer_style))
    story.append(Paragraph("小白设计工作室 | 2026年2月28日", footer_style))
    
    doc.build(story)
    
    print(f"✅ V4优化版报告已生成: {pdf_file}")
    print(f"📄 文件大小: {os.path.getsize(pdf_file)/1024:.1f} KB")
    return pdf_file

if __name__ == "__main__":
    print("🎨 生成V4优化版案例研习报告...")
    print("=" * 60)
    result = create_report()
    print("=" * 60)
    print("🎉 完成！")
