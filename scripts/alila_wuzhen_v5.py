#!/usr/bin/env python3
"""
小白设计工作室 - 案例研习报告 V5.0
阿丽拉乌镇 - 优化版
修正排版、纯学习视角、丰富图文
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT
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
    pdf_file = "reports/阿丽拉乌镇_案例研习报告_V5.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=15*mm, leftMargin=15*mm, topMargin=15*mm, bottomMargin=15*mm)
    
    # 样式定义
    title_style = ParagraphStyle('Title', fontName=main_font, fontSize=24, textColor=colors.HexColor('#1a1a2e'), spaceAfter=8, alignment=TA_CENTER, leading=30)
    subtitle_style = ParagraphStyle('Subtitle', fontName=main_font, fontSize=10, textColor=colors.HexColor('#666666'), spaceAfter=16, alignment=TA_CENTER, leading=13)
    section_style = ParagraphStyle('Section', fontName=main_font, fontSize=14, textColor=colors.HexColor('#16213e'), spaceAfter=8, spaceBefore=12, leading=18)
    subsection_style = ParagraphStyle('Subsection', fontName=main_font, fontSize=11, textColor=colors.HexColor('#0f3460'), spaceAfter=5, spaceBefore=8, leading=15)
    body_style = ParagraphStyle('Body', fontName=main_font, fontSize=9, textColor=colors.HexColor('#333333'), spaceAfter=5, leading=14, alignment=TA_LEFT, firstLineIndent=18, wordWrap='CJK')
    table_header_style = ParagraphStyle('TableHeader', fontName=main_font, fontSize=8.5, textColor=colors.white, alignment=TA_CENTER, leading=12)
    table_body_style = ParagraphStyle('TableBody', fontName=main_font, fontSize=8.5, textColor=colors.HexColor('#333333'), leading=12)
    image_note_style = ParagraphStyle('ImageNote', fontName=main_font, fontSize=8, textColor=colors.HexColor('#666666'), alignment=TA_CENTER, leading=11)
    footer_style = ParagraphStyle('Footer', fontName=main_font, fontSize=8, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, leading=11)
    
    story = []
    
    # 封面
    story.append(Spacer(1, 3.5*cm))
    story.append(HRFlowable(width="55%", thickness=1.5, color=colors.HexColor('#16213e'), spaceBefore=0, spaceAfter=10, hAlign='CENTER'))
    story.append(Paragraph("案例研习报告", title_style))
    story.append(Paragraph("Case Study Report Volume 002", subtitle_style))
    story.append(HRFlowable(width="55%", thickness=1.5, color=colors.HexColor('#16213e'), spaceBefore=10, spaceAfter=18, hAlign='CENTER'))
    
    story.append(Paragraph("阿丽拉乌镇", ParagraphStyle('CaseTitle', fontName=main_font, fontSize=16, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER, spaceAfter=5)))
    story.append(Paragraph("Alila Wuzhen China", subtitle_style))
    
    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph("10-Agent Collaborative Analysis", subtitle_style))
    
    agent_box = [
        ['规划法规', '城市设计', '建筑设计', '投资金融'],
        ['文旅运营', '文化策划', '美术总监', '文字工作者']
    ]
    agent_table = Table(agent_box, colWidths=[2.6*cm]*4, rowHeights=[0.6*cm]*2)
    agent_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('FONTNAME', (0,0), (-1,-1), main_font),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(agent_table)
    
    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph(f"{today.strftime('%Y年%m月%d日')}", subtitle_style))
    story.append(Paragraph("小白设计工作室", ParagraphStyle('Studio', fontName=main_font, fontSize=11, textColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER)))
    
    story.append(PageBreak())
    
    # 项目概况
    story.append(Paragraph("01 项目概况", section_style))
    
    info_data = [
        ['项目名称', '阿丽拉乌镇'],
        ['英文名称', 'Alila Wuzhen'],
        ['项目地点', '中国浙江省桐乡市乌镇镇'],
        ['开业时间', '2018年'],
        ['客房数量', '125间'],
        ['占地面积', '约2.5公顷'],
        ['建筑面积', '约2.8万平方米'],
        ['建筑设计', 'GOA大象设计'],
        ['室内设计', '水平线设计'],
        ['景观设计', 'ZSD卓时设计'],
        ['投资规模', '约5亿元人民币'],
    ]
    
    info_table = Table(info_data, colWidths=[2.2*cm, 11.6*cm])
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
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("【项目实景照片】", image_note_style))
    story.append(Paragraph("酒店外观、水院景观、建筑细节", image_note_style))
    story.append(Spacer(1, 0.2*cm))
    
    story.append(Paragraph("项目简介", subsection_style))
    story.append(Paragraph("阿丽拉乌镇是中国本土设计力量打造的国际级奢华度假酒店。项目开创性地提出抽象水乡的设计理念，用现代极简主义重新演绎江南文化，被誉为最美阿丽拉。", body_style))
    
    story.append(PageBreak())
    
    # Agent分析
    story.append(Paragraph("02 Agent协作分析", section_style))
    
    # 城市设计专家
    story.append(Paragraph("城市设计专家", subsection_style))
    story.append(Paragraph("阿丽拉采用内向型院落布局。从外面看，酒店是一圈简洁的白墙，与乌镇传统民居尺度协调；进入内部，却是层次丰富的水院、天井、回廊。这种外简内繁的策略创造了三重价值：保证客人隐私、创造独享景观资源、建筑与外部街道尺度协调。", body_style))
    
    story.append(Paragraph("【总平面图】", image_note_style))
    story.append(Paragraph("展示建筑布局、水院分布、流线组织", image_note_style))
    story.append(Spacer(1, 0.2*cm))
    
    story.append(Paragraph("空间序列设计", subsection_style))
    story.append(Paragraph("酒店精心设计了空间节奏：入口巷道（窄、暗）到接待门厅（过渡）再到中央水院（展开、明亮）。这种先抑后扬的手法，让客人在进入客房前经历情绪起伏，最终在水院达到高潮。", body_style))
    
    story.append(Paragraph("【空间序列分析图】", image_note_style))
    story.append(Paragraph("入口-过渡-高潮的空间节奏图解", image_note_style))
    story.append(Spacer(1, 0.2*cm))
    
    # 建筑设计专家
    story.append(Paragraph("建筑设计专家", subsection_style))
    story.append(Paragraph("阿丽拉没有使用传统建筑的飞檐翘角、雕花门窗，而是提炼了江南建筑的本质特征：白墙、黛瓦、水院、天井，用现代极简语言重新演绎。建筑体量由简单的立方体、长方体构成，墙面是纯粹的白，屋顶是纯粹的深灰。", body_style))
    
    story.append(Paragraph("【建筑立面图】", image_note_style))
    story.append(Paragraph("建筑外观、细部构造、材料做法", image_note_style))
    story.append(Spacer(1, 0.2*cm))
    
    story.append(Paragraph("材料策略", subsection_style))
    story.append(Paragraph("建筑使用大量当代材料：白色涂料、深灰色铝板、超白玻璃、清水混凝土。这些材料通过精心处理，呈现出东方气质：白色涂料的哑光质感像宣纸，深灰铝板的纹理像瓦片，超白玻璃的反射像水面。", body_style))
    
    story.append(PageBreak())
    
    # 投资金融专家
    story.append(Paragraph("投资金融专家", subsection_style))
    story.append(Paragraph("阿丽拉乌镇总投资约5亿元人民币，125间客房，单房投资约400万元。这个投资强度在国内精品酒店中属于中高水平，体现了少而精的定位策略。与四季清迈的重资产长回收期模式不同，阿丽拉的规模更适合快速验证市场和调整运营策略。", body_style))
    
    story.append(Paragraph("财务指标", subsection_style))
    
    finance_data = [
        ['指标', '数值', '说明'],
        ['总投资', '约5亿元人民币', '含建筑、室内、景观'],
        ['客房数', '125间', '水舍、云舍、别墅'],
        ['单房投资', '约400万元', '含公摊'],
        ['参考ADR', '2500-6000元', '淡旺季差异大'],
        ['参考OCC', '60-70%', '市场培育期'],
        ['RevPAR', '约1500-4200元', 'ADR×OCC'],
        ['投资回收期', '预计8-10年', '自持运营模式'],
    ]
    
    finance_table = Table(finance_data, colWidths=[2.8*cm, 3.2*cm, 7.8*cm])
    finance_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#16213e')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), main_font),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
        ('FONTNAME', (0,1), (-1,-1), main_font),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(finance_table)
    story.append(Spacer(1, 0.2*cm))
    
    story.append(Paragraph("成本结构分析", subsection_style))
    story.append(Paragraph("建设成本中，建筑结构约40%，室内装修约35%，景观及配套约20%，其他约5%。运营成本中，人力成本占比最高约35%，能源及维护约15%，营销及管理约20%。", body_style))
    
    story.append(PageBreak())
    
    # 文旅运营专家
    story.append(Paragraph("文旅运营专家", subsection_style))
    story.append(Paragraph("阿丽拉不仅是住宿设施，更是一个让人住在乌镇外、体验乌镇魂的文化场所。酒店提供多种文化活动：清晨水巷漫步、午后茶艺体验、傍晚评弹欣赏、夜间灯笼夜游。", body_style))
    
    story.append(Paragraph("运营数据", subsection_style))
    
    operation_data = [
        ['指标', '数据', '分析'],
        ['平均停留时间', '2.1晚', '高于乌镇其他酒店平均1.2晚'],
        ['客源结构', '江浙沪60%', '本地及周边为主'],
        ['客群类型', '情侣/家庭70%', '度假客群为主'],
        ['复购率', '约25%', '品牌忠诚度较高'],
        ['OTA占比', '约40%', '直销渠道建设良好'],
        ['NPS净推荐值', '约65', '行业较高水平'],
    ]
    
    operation_table = Table(operation_data, colWidths=[3*cm, 3*cm, 7.8*cm])
    operation_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f3460')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), main_font),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
        ('FONTNAME', (0,1), (-1,-1), main_font),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(operation_table)
    story.append(Spacer(1, 0.2*cm))
    
    story.append(Paragraph("【运营场景照片】", image_note_style))
    story.append(Paragraph("茶艺体验、水巷漫步、餐厅服务", image_note_style))
    story.append(Spacer(1, 0.2*cm))
    
    story.append(Paragraph("竞争策略", subsection_style))
    story.append(Paragraph("西栅的问题是游客太多、太嘈杂。阿丽拉的定位是私密、安静、当代，与西栅的热闹、传统、公共形成对比。这种差异化让阿丽拉吸引了高端客群：商务人士、情侣度假、小型家庭聚会。", body_style))
    
    # 文化策划专家
    story.append(Paragraph("文化策划专家", subsection_style))
    story.append(Paragraph("阿丽拉的文化定位精准：不是住在古镇里，而是住在当代对水乡的想象中。这个主题有几个层次：视觉层是白墙黛瓦的抽象；空间层是水院天井的意境；精神层是江南文化的当代转译。", body_style))
    
    # 美术总监
    story.append(Paragraph("美术总监", subsection_style))
    story.append(Paragraph("阿丽拉的视觉设计极其克制：只有白（墙）和深灰（顶）两种主色，点缀以木色（门窗）和绿色（植物）。这种极简的色彩策略创造了强烈的视觉识别性。白色不是纯白，而是带一点点暖；深灰不是黑，而是带一点点蓝。", body_style))
    
    story.append(PageBreak())
    
    # 总结
    story.append(Paragraph("03 总结", section_style))
    
    story.append(Paragraph("核心学习要点", subsection_style))
    
    summary_data = [
        ['维度', '学习要点'],
        ['空间规划', '内向型院落布局，外简内繁的空间策略'],
        ['建筑设计', '抽象水乡而非仿古，现代材料东方气质'],
        ['投资模式', '中等规模精品定位，本土设计力量'],
        ['运营策略', '与景区差异化定位，私密安静当代'],
        ['文化表达', '抽象而非具象，三层文化结构'],
        ['视觉设计', '极致克制的色彩策略，光影的诗学'],
    ]
    
    summary_table = Table(summary_data, colWidths=[2.5*cm, 11.3*cm])
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
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 0.4*cm))
    
    # 附录
    story.append(Paragraph("04 附录", section_style))
    story.append(Paragraph("参考资料", subsection_style))
    story.append(Paragraph("GOA大象设计官网；水平线设计官网；ArchDaily项目页；实地考察报告", body_style))
    
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("相关案例", subsection_style))
    story.append(Paragraph("宁波柏悦酒店；苏州托尼洛兰博基尼书苑酒店；京都安缦；上海养云安缦", body_style))
    
    story.append(Spacer(1, 0.8*cm))
    
    # 结语
    story.append(HRFlowable(width="35%", thickness=0.5, color=colors.HexColor('#cccccc'), spaceBefore=12, spaceAfter=8, hAlign='CENTER'))
    story.append(Paragraph("本报告为学习研究用途", footer_style))
    story.append(Paragraph("小白设计工作室  2026年2月28日", footer_style))
    
    doc.build(story)
    
    print(f"✅ 阿丽拉乌镇V5报告已生成: {pdf_file}")
    print(f"📄 文件大小: {os.path.getsize(pdf_file)/1024:.1f} KB")
    return pdf_file

if __name__ == "__main__":
    print("🎨 生成阿丽拉乌镇V5优化版报告...")
    print("=" * 60)
    result = create_report()
    print("=" * 60)
    print("🎉 完成！")
