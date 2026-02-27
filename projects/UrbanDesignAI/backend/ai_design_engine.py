# AI设计生成引擎
# 基于大语言模型生成设计方案

import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

@dataclass
class DesignConcept:
    """设计理念"""
    theme: str  # 主题
    philosophy: str  # 设计理念
    spatial_structure: str  # 空间结构
    functional_layout: str  # 功能布局思路
    landscape_strategy: str  # 景观策略

def generate_design_prompt(constraints, boundary, site_analysis) -> str:
    """
    生成AI设计提示词
    
    Args:
        constraints: 设计限制条件
        boundary: 用地边界
        site_analysis: 场地分析结果
    
    Returns:
        给AI的提示词
    """
    prompt = f"""
你是一位资深的城市规划设计师，拥有20年文旅项目设计经验。
请根据以下用地条件和限制参数，设计一个创新的{constraints.function_type}方案。

## 用地条件
- 用地面积: {boundary.area:.2f} 平方米
- 用地形状: {site_analysis['shape_type']}
- 长宽比: {site_analysis['aspect_ratio']:.2f}
- 不规则度: {site_analysis['irregularity']:.2f}

## 设计限制条件
- 容积率: {constraints.plot_ratio}
- 建筑密度: {constraints.building_density}%
- 绿化率: {constraints.green_rate}%
- 限高: {constraints.height_limit}米
- 功能定位: {constraints.function_type}

## 设计要求
1. 结合用地特点，提出创新的空间布局方案
2. 满足所有规划指标要求
3. 考虑人流组织和景观视线
4. 提出具有地域文化特色的设计理念

## 输出格式
请用中文输出以下内容：

### 1. 设计主题
（一句话概括设计主题）

### 2. 设计理念
（阐述设计的核心理念，200字左右）

### 3. 空间结构
（描述整体空间布局，包括功能分区）

### 4. 功能布局
（详细描述各个功能区的位置关系）

### 5. 景观策略
（景观设计思路，绿化、水系、公共空间等）

### 6. 建筑形态建议
（建筑风格、高度控制、体量关系）
"""
    return prompt

def parse_ai_design_response(response_text: str) -> Dict:
    """
    解析AI返回的设计方案
    
    Args:
        response_text: AI的原始回复
    
    Returns:
        结构化的设计方案
    """
    design = {
        "theme": "",
        "philosophy": "",
        "spatial_structure": "",
        "functional_layout": "",
        "landscape_strategy": "",
        "building_form": ""
    }
    
    # 简单的文本解析
    sections = response_text.split("###")
    
    for section in sections:
        if "设计主题" in section:
            design["theme"] = extract_content(section)
        elif "设计理念" in section:
            design["philosophy"] = extract_content(section)
        elif "空间结构" in section:
            design["spatial_structure"] = extract_content(section)
        elif "功能布局" in section:
            design["functional_layout"] = extract_content(section)
        elif "景观策略" in section:
            design["landscape_strategy"] = extract_content(section)
        elif "建筑形态" in section:
            design["building_form"] = extract_content(section)
    
    return design

def extract_content(section: str) -> str:
    """从章节中提取内容"""
    lines = section.strip().split('\n')
    # 去掉标题行
    if len(lines) > 1:
        return '\n'.join(lines[1:]).strip()
    return section.strip()

def generate_functional_zones(constraints, boundary) -> List[Dict]:
    """
    生成功能分区建议
    
    Returns:
        功能分区列表
    """
    zones = []
    
    if constraints.function_type == "文旅小镇":
        zones = [
            {"name": "核心文化展示区", "area_ratio": 0.15, "description": "主题文化体验、演艺活动"},
            {"name": "商业休闲区", "area_ratio": 0.25, "description": "特色餐饮、文创零售、休闲娱乐"},
            {"name": "住宿度假区", "area_ratio": 0.30, "description": "精品民宿、度假酒店"},
            {"name": "景观游憩区", "area_ratio": 0.20, "description": "园林绿地、水系景观、步行系统"},
            {"name": "配套服务区", "area_ratio": 0.10, "description": "游客中心、停车、后勤配套"}
        ]
    elif constraints.function_type == "住宅":
        zones = [
            {"name": "高层住宅", "area_ratio": 0.40, "description": "主力住宅产品"},
            {"name": "洋房/别墅", "area_ratio": 0.20, "description": "高端住宅产品"},
            {"name": "公共绿地", "area_ratio": 0.20, "description": "社区公园、景观节点"},
            {"name": "配套设施", "area_ratio": 0.15, "description": "幼儿园、商业、会所"},
            {"name": "道路停车", "area_ratio": 0.05, "description": "道路系统、停车场"}
        ]
    elif constraints.function_type == "商业":
        zones = [
            {"name": "主力商业", "area_ratio": 0.40, "description": "购物中心、百货"},
            {"name": "街区商业", "area_ratio": 0.25, "description": "步行街、餐饮娱乐"},
            {"name": "办公商务", "area_ratio": 0.20, "description": "写字楼、商务公寓"},
            {"name": "公共空间", "area_ratio": 0.15, "description": "广场、绿地、停车"}
        ]
    
    # 计算实际面积
    for zone in zones:
        zone["area"] = boundary.area * zone["area_ratio"]
    
    return zones

def generate_design_logic_text(design_concept: Dict, zones: List[Dict]) -> str:
    """
    生成设计逻辑说明文字
    
    Returns:
        设计逻辑文档
    """
    text = f"""# 设计逻辑与理念

## 一、设计主题
{design_concept.get('theme', '待定')}

## 二、设计理念
{design_concept.get('philosophy', '待定')}

## 三、空间结构策略
{design_concept.get('spatial_structure', '待定')}

## 四、功能布局逻辑
{design_concept.get('functional_layout', '待定')}

### 功能分区详情
"""
    
    for i, zone in enumerate(zones, 1):
        text += f"""
**{i}. {zone['name']}**
- 面积占比: {zone['area_ratio']*100:.1f}%
- 建议面积: {zone['area']:.0f} ㎡
- 功能说明: {zone['description']}
"""
    
    text += f"""
## 五、景观设计策略
{design_concept.get('landscape_strategy', '待定')}

## 六、建筑形态控制
{design_concept.get('building_form', '待定')}

## 七、设计亮点
1. 充分利用用地特点，打造特色空间
2. 合理组织功能分区，优化人流动线
3. 注重景观渗透，创造宜人环境
4. 体现地域文化，塑造场所精神

---
*本方案由AI辅助生成，供设计参考使用*
"""
    
    return text

if __name__ == "__main__":
    print("🎨 AI设计生成引擎测试")
    
    # 测试功能分区生成
    from cad_handler import generate_sample_boundary, DesignConstraints
    
    boundary = generate_sample_boundary()
    constraints = DesignConstraints(
        plot_ratio=1.5,
        building_density=35.0,
        green_rate=30.0,
        height_limit=24.0,
        land_area=boundary.area,
        function_type="文旅小镇"
    )
    
    zones = generate_functional_zones(constraints, boundary)
    print("\n📋 功能分区建议:")
    for zone in zones:
        print(f"  {zone['name']}: {zone['area_ratio']*100:.1f}% ({zone['area']:.0f}㎡)")
    
    # 测试提示词生成
    site_analysis = {
        "shape_type": "不规则多边形",
        "aspect_ratio": 1.5,
        "irregularity": 0.3
    }
    
    prompt = generate_design_prompt(constraints, boundary, site_analysis)
    print(f"\n📝 生成的AI提示词长度: {len(prompt)} 字符")
    print("提示词已准备好，可以发送给AI生成设计方案")
