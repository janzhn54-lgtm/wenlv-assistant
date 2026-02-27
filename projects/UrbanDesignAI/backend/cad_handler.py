# UrbanDesignAI - 城市规划设计AI助手
# MVP版本：核心功能实现

import os
import json
import ezdxf
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import numpy as np

@dataclass
class DesignConstraints:
    """设计限制条件"""
    plot_ratio: float  # 容积率
    building_density: float  # 建筑密度 (%)
    green_rate: float  # 绿化率 (%)
    height_limit: float  # 限高 (米)
    land_area: float  # 用地面积 (平方米)
    function_type: str  # 功能类型：文旅小镇/住宅/商业/混合
    
@dataclass
class LandBoundary:
    """用地红线数据"""
    points: List[Tuple[float, float]]  # 多边形顶点坐标
    area: float  # 面积
    boundary_length: float  # 周长

def read_cad_boundary(file_path: str) -> LandBoundary:
    """
    读取CAD红线图，提取用地边界
    
    Args:
        file_path: CAD文件路径 (.dwg 或 .dxf)
    
    Returns:
        LandBoundary: 用地边界数据
    """
    try:
        # 读取DXF文件
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()
        
        # 查找红线（通常在特定图层）
        boundary_points = []
        for entity in msp:
            if entity.dxftype() == 'LWPOLYLINE':
                # 获取多边形顶点
                points = [(p[0], p[1]) for p in entity.get_points()]
                boundary_points = points
                break
        
        # 计算面积（使用鞋带公式）
        area = calculate_polygon_area(boundary_points)
        
        # 计算周长
        perimeter = calculate_perimeter(boundary_points)
        
        return LandBoundary(
            points=boundary_points,
            area=area,
            boundary_length=perimeter
        )
    except Exception as e:
        print(f"读取CAD文件失败: {e}")
        # 返回示例数据用于测试
        return generate_sample_boundary()

def calculate_polygon_area(points: List[Tuple[float, float]]) -> float:
    """计算多边形面积（鞋带公式）"""
    n = len(points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def calculate_perimeter(points: List[Tuple[float, float]]) -> float:
    """计算多边形周长"""
    n = len(points)
    perimeter = 0.0
    for i in range(n):
        j = (i + 1) % n
        dx = points[j][0] - points[i][0]
        dy = points[j][1] - points[i][1]
        perimeter += np.sqrt(dx**2 + dy**2)
    return perimeter

def generate_sample_boundary() -> LandBoundary:
    """生成示例用地边界（用于测试）"""
    # 创建一个不规则四边形，模拟真实用地
    points = [
        (0, 0),
        (100, 0),
        (120, 80),
        (80, 100),
        (20, 90),
        (0, 50)
    ]
    area = calculate_polygon_area(points)
    perimeter = calculate_perimeter(points)
    
    return LandBoundary(
        points=points,
        area=area,
        boundary_length=perimeter
    )

def validate_constraints(constraints: DesignConstraints, boundary: LandBoundary) -> Dict:
    """
    验证设计限制条件是否可行
    
    Returns:
        验证结果字典
    """
    results = {
        "valid": True,
        "messages": [],
        "suggestions": []
    }
    
    # 检查容积率
    max_plot_ratio = 3.0  # 假设最大容积率3.0
    if constraints.plot_ratio > max_plot_ratio:
        results["valid"] = False
        results["messages"].append(f"容积率{constraints.plot_ratio}超过最大限制{max_plot_ratio}")
    
    # 检查建筑密度
    if constraints.building_density > 50:
        results["valid"] = False
        results["messages"].append(f"建筑密度{constraints.building_density}%过高")
    
    # 检查绿化率
    if constraints.green_rate < 20:
        results["suggestions"].append(f"绿化率{constraints.green_rate}%偏低，建议提高")
    
    # 计算理论最大建筑面积
    max_building_area = boundary.area * constraints.plot_ratio
    results["max_building_area"] = max_building_area
    
    return results

def analyze_site_conditions(boundary: LandBoundary) -> Dict:
    """
    分析场地条件
    
    Returns:
        场地分析结果
    """
    analysis = {
        "shape_type": analyze_shape(boundary.points),
        "area_category": categorize_area(boundary.area),
        "aspect_ratio": calculate_aspect_ratio(boundary.points),
        "irregularity": calculate_irregularity(boundary.points)
    }
    return analysis

def analyze_shape(points: List[Tuple[float, float]]) -> str:
    """分析用地形状类型"""
    n = len(points)
    if n == 4:
        return "四边形"
    elif n == 3:
        return "三角形"
    elif n > 6:
        return "不规则多边形"
    else:
        return f"{n}边形"

def categorize_area(area: float) -> str:
    """按面积分类用地规模"""
    if area < 10000:
        return "小型用地 (<1万㎡)"
    elif area < 50000:
        return "中型用地 (1-5万㎡)"
    elif area < 100000:
        return "大型用地 (5-10万㎡)"
    else:
        return "超大型用地 (>10万㎡)"

def calculate_aspect_ratio(points: List[Tuple[float, float]]) -> float:
    """计算长宽比"""
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    return max(width, height) / min(width, height)

def calculate_irregularity(points: List[Tuple[float, float]]) -> float:
    """计算不规则度（0-1，越接近1越不规则）"""
    # 简化的不规则度计算
    area = calculate_polygon_area(points)
    perimeter = calculate_perimeter(points)
    # 圆形度指标
    circularity = 4 * np.pi * area / (perimeter ** 2)
    return 1 - circularity

if __name__ == "__main__":
    # 测试代码
    print("🚀 UrbanDesignAI CAD处理模块测试")
    
    # 生成示例用地
    boundary = generate_sample_boundary()
    print(f"\n📐 用地信息:")
    print(f"   面积: {boundary.area:.2f} ㎡")
    print(f"   周长: {boundary.boundary_length:.2f} m")
    print(f"   顶点数: {len(boundary.points)}")
    
    # 场地分析
    analysis = analyze_site_conditions(boundary)
    print(f"\n📊 场地分析:")
    for key, value in analysis.items():
        print(f"   {key}: {value}")
    
    # 设计限制条件示例
    constraints = DesignConstraints(
        plot_ratio=1.5,
        building_density=35.0,
        green_rate=30.0,
        height_limit=24.0,
        land_area=boundary.area,
        function_type="文旅小镇"
    )
    
    # 验证限制条件
    validation = validate_constraints(constraints, boundary)
    print(f"\n✅ 限制条件验证:")
    print(f"   可行: {validation['valid']}")
    print(f"   最大建筑面积: {validation['max_building_area']:.2f} ㎡")
