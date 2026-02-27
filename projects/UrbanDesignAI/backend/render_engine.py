# 渲染图生成模块
# 生成彩色平面图、鸟瞰图、人视图

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Circle, Rectangle
import numpy as np
from typing import List, Tuple, Dict
import json

def generate_colored_plan(boundary_points: List[Tuple[float, float]], 
                         zones: List[Dict],
                         output_path: str = "colored_plan.png"):
    """
    生成彩色平面图
    
    Args:
        boundary_points: 用地边界点
        zones: 功能分区列表
        output_path: 输出路径
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 颜色方案
    colors = {
        "核心文化展示区": "#E74C3C",  # 红色
        "商业休闲区": "#F39C12",      # 橙色
        "住宿度假区": "#3498DB",      # 蓝色
        "景观游憩区": "#2ECC71",      # 绿色
        "配套服务区": "#95A5A6",      # 灰色
        "高层住宅": "#9B59B6",        # 紫色
        "洋房/别墅": "#3498DB",       # 蓝色
        "公共绿地": "#2ECC71",        # 绿色
        "配套设施": "#F1C40F",        # 黄色
        "道路停车": "#BDC3C7",        # 浅灰
        "主力商业": "#E74C3C",        # 红色
        "街区商业": "#F39C12",        # 橙色
        "办公商务": "#3498DB",        # 蓝色
        "公共空间": "#2ECC71"         # 绿色
    }
    
    # 绘制用地边界
    boundary = Polygon(boundary_points, fill=False, 
                      edgecolor='#E74C3C', linewidth=3, linestyle='--')
    ax.add_patch(boundary)
    
    # 绘制功能分区（简化版，在用地内部随机分布）
    # 实际项目中需要根据算法精确计算分区位置
    np.random.seed(42)
    center_x = np.mean([p[0] for p in boundary_points])
    center_y = np.mean([p[1] for p in boundary_points])
    
    for i, zone in enumerate(zones):
        # 计算分区位置（简化演示）
        angle = 2 * np.pi * i / len(zones)
        radius = 20 + i * 5
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        
        # 分区大小根据面积比例
        size = np.sqrt(zone['area_ratio']) * 30
        
        color = colors.get(zone['name'], '#3498DB')
        
        # 绘制分区（用矩形代替，实际应为不规则形状）
        rect = Rectangle((x - size/2, y - size/2), size, size,
                        facecolor=color, edgecolor='white', 
                        linewidth=2, alpha=0.7)
        ax.add_patch(rect)
        
        # 添加文字标签
        ax.text(x, y, zone['name'], ha='center', va='center',
               fontsize=8, fontweight='bold', color='white',
               bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))
    
    # 添加指北针
    ax.annotate('N', xy=(0.95, 0.95), xycoords='axes fraction',
               fontsize=20, ha='center', va='center',
               bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black'))
    ax.annotate('', xy=(0.95, 0.88), xytext=(0.95, 0.95),
               xycoords='axes fraction',
               arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    # 添加比例尺
    scale_x = min([p[0] for p in boundary_points]) + 5
    scale_y = min([p[1] for p in boundary_points]) - 10
    ax.plot([scale_x, scale_x + 50], [scale_y, scale_y], 'k-', linewidth=3)
    ax.text(scale_x + 25, scale_y - 5, '50m', ha='center', fontsize=10)
    
    # 设置坐标轴
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('距离 (米)', fontsize=12)
    ax.set_ylabel('距离 (米)', fontsize=12)
    ax.set_title('彩色总平面图', fontsize=16, fontweight='bold')
    
    # 添加图例
    legend_elements = [patches.Patch(facecolor=colors.get(zone['name'], '#3498DB'),
                                     label=f"{zone['name']} ({zone['area_ratio']*100:.0f}%)")
                      for zone in zones]
    ax.legend(handles=legend_elements, loc='upper left', 
             bbox_to_anchor=(1.02, 1), fontsize=10)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight',
               facecolor='white', edgecolor='none')
    plt.close()
    
    print(f"✅ 彩色平面图已生成: {output_path}")
    return output_path

def generate_bird_eye_view(boundary_points: List[Tuple[float, float]],
                          zones: List[Dict],
                          output_path: str = "bird_eye_view.png"):
    """
    生成鸟瞰效果图
    
    注意：这是简化版，实际项目应使用3D渲染引擎（Blender）
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 绘制基地
    boundary = Polygon(boundary_points, fill=True, 
                      facecolor='#E8F5E9', edgecolor='#2E7D32', 
                      linewidth=2, alpha=0.5)
    ax.add_patch(boundary)
    
    # 模拟建筑（简化版鸟瞰）
    np.random.seed(42)
    for i, zone in enumerate(zones):
        if "建筑" in zone['name'] or "住宅" in zone['name'] or "商业" in zone['name']:
            # 在分区内绘制建筑方块
            n_buildings = max(3, int(zone['area_ratio'] * 10))
            for j in range(n_buildings):
                x = np.random.uniform(min([p[0] for p in boundary_points]) + 10,
                                     max([p[0] for p in boundary_points]) - 10)
                y = np.random.uniform(min([p[1] for p in boundary_points]) + 10,
                                     max([p[1] for p in boundary_points]) - 10)
                
                width = np.random.uniform(8, 20)
                height = np.random.uniform(8, 20)
                
                # 建筑阴影（模拟3D效果）
                shadow = Rectangle((x+2, y-2), width, height,
                                  facecolor='gray', alpha=0.3)
                ax.add_patch(shadow)
                
                # 建筑主体
                building = Rectangle((x, y), width, height,
                                    facecolor='#5C6BC0', edgecolor='#3F51B5',
                                    linewidth=1, alpha=0.8)
                ax.add_patch(building)
                
                # 屋顶
                roof = Polygon([(x, y+height), (x+width/2, y+height+3), 
                              (x+width, y+height)],
                             facecolor='#7986CB', edgecolor='#3F51B5', linewidth=1)
                ax.add_patch(roof)
    
    # 添加树木（绿点）
    for _ in range(30):
        x = np.random.uniform(min([p[0] for p in boundary_points]) + 5,
                             max([p[0] for p in boundary_points]) - 5)
        y = np.random.uniform(min([p[1] for p in boundary_points]) + 5,
                             max([p[1] for p in boundary_points]) - 5)
        tree = Circle((x, y), 1.5, facecolor='#4CAF50', edgecolor='#2E7D32', alpha=0.7)
        ax.add_patch(tree)
    
    # 设置样式
    ax.set_aspect('equal')
    ax.set_xlim(min([p[0] for p in boundary_points]) - 10,
               max([p[0] for p in boundary_points]) + 10)
    ax.set_ylim(min([p[1] for p in boundary_points]) - 10,
               max([p[1] for p in boundary_points]) + 10)
    ax.axis('off')
    ax.set_title('鸟瞰效果图（示意）', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight',
               facecolor='white', edgecolor='none')
    plt.close()
    
    print(f"✅ 鸟瞰图已生成: {output_path}")
    return output_path

def generate_analysis_diagrams(boundary_points: List[Tuple[float, float]],
                               zones: List[Dict],
                               output_dir: str = "analysis"):
    """
    生成设计分析图
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    diagrams = []
    
    # 1. 功能分区分析图
    fig, ax = plt.subplots(figsize=(10, 8))
    colors_list = plt.cm.Set3(np.linspace(0, 1, len(zones)))
    
    for i, zone in enumerate(zones):
        # 绘制饼图展示面积比例
        pass  # 饼图单独绘制
    
    # 绘制分区图
    boundary = Polygon(boundary_points, fill=False, 
                      edgecolor='black', linewidth=2)
    ax.add_patch(boundary)
    
    # 添加分区标注
    np.random.seed(42)
    for i, zone in enumerate(zones):
        angle = 2 * np.pi * i / len(zones)
        x = np.mean([p[0] for p in boundary_points]) + 30 * np.cos(angle)
        y = np.mean([p[1] for p in boundary_points]) + 30 * np.sin(angle)
        ax.text(x, y, f"{i+1}", ha='center', va='center',
               fontsize=14, fontweight='bold',
               bbox=dict(boxstyle='circle', facecolor=colors_list[i], 
                        edgecolor='black', linewidth=2))
    
    ax.set_aspect('equal')
    ax.set_title('功能分区分析图', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    path1 = f"{output_dir}/zoning_analysis.png"
    plt.savefig(path1, dpi=150, bbox_inches='tight')
    plt.close()
    diagrams.append(path1)
    
    # 2. 面积分配饼图
    fig, ax = plt.subplots(figsize=(8, 8))
    labels = [f"{z['name']}\n{z['area_ratio']*100:.1f}%" for z in zones]
    sizes = [z['area_ratio'] for z in zones]
    colors = colors_list[:len(zones)]
    
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors,
                                       autopct='', startangle=90,
                                       textprops={'fontsize': 10})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('功能面积分配图', fontsize=14, fontweight='bold')
    
    path2 = f"{output_dir}/area_distribution.png"
    plt.savefig(path2, dpi=150, bbox_inches='tight')
    plt.close()
    diagrams.append(path2)
    
    print(f"✅ 分析图已生成: {len(diagrams)} 张")
    return diagrams

if __name__ == "__main__":
    print("🎨 渲染图生成模块测试")
    
    # 测试数据
    from cad_handler import generate_sample_boundary
    from ai_design_engine import generate_functional_zones
    from cad_handler import DesignConstraints
    
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
    
    # 生成彩色平面图
    generate_colored_plan(boundary.points, zones, 
                         "/home/codespace/.openclaw/workspace/projects/UrbanDesignAI/outputs/colored_plan.png")
    
    # 生成鸟瞰图
    generate_bird_eye_view(boundary.points, zones,
                          "/home/codespace/.openclaw/workspace/projects/UrbanDesignAI/outputs/bird_eye_view.png")
    
    # 生成分析图
    generate_analysis_diagrams(boundary.points, zones,
                              "/home/codespace/.openclaw/workspace/projects/UrbanDesignAI/outputs/analysis")
    
    print("\n✅ 所有渲染图生成完成！")
    print("查看 outputs/ 目录")
