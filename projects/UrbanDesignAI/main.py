#!/usr/bin/env python3
# UrbanDesignAI - 主程序入口
# AI城市规划设计助手

import os
import sys
import json
from datetime import datetime

# 添加后端模块路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from cad_handler import (
    read_cad_boundary, 
    generate_sample_boundary,
    DesignConstraints,
    validate_constraints,
    analyze_site_conditions
)
from ai_design_engine import (
    generate_functional_zones,
    generate_design_prompt,
    generate_design_logic_text
)
from render_engine import (
    generate_colored_plan,
    generate_bird_eye_view,
    generate_analysis_diagrams
)

class UrbanDesignAI:
    """AI城市规划设计助手主类"""
    
    def __init__(self):
        self.project_name = ""
        self.boundary = None
        self.constraints = None
        self.site_analysis = None
        self.zones = None
        self.design_concept = None
        self.output_dir = "outputs"
        
        # 确保输出目录存在
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "analysis"), exist_ok=True)
    
    def load_project(self, cad_file_path: str, constraints_dict: dict, project_name: str = ""):
        """
        加载项目信息
        
        Args:
            cad_file_path: CAD文件路径
            constraints_dict: 限制条件字典
            project_name: 项目名称
        """
        print(f"\n{'='*60}")
        print(f"🏙️  UrbanDesignAI - 项目启动")
        print(f"{'='*60}\n")
        
        self.project_name = project_name or f"项目_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # 1. 读取CAD红线图
        print("📐 步骤1: 读取用地红线图...")
        if os.path.exists(cad_file_path):
            self.boundary = read_cad_boundary(cad_file_path)
            print(f"   ✅ CAD文件已加载: {cad_file_path}")
        else:
            print(f"   ⚠️  CAD文件不存在，使用示例数据")
            self.boundary = generate_sample_boundary()
        
        print(f"   📊 用地面积: {self.boundary.area:.2f} ㎡")
        print(f"   📏 周长: {self.boundary.boundary_length:.2f} m")
        
        # 2. 设置限制条件
        print("\n📋 步骤2: 设置设计限制条件...")
        self.constraints = DesignConstraints(
            plot_ratio=constraints_dict.get('plot_ratio', 1.5),
            building_density=constraints_dict.get('building_density', 35.0),
            green_rate=constraints_dict.get('green_rate', 30.0),
            height_limit=constraints_dict.get('height_limit', 24.0),
            land_area=self.boundary.area,
            function_type=constraints_dict.get('function_type', '文旅小镇')
        )
        
        print(f"   📌 功能定位: {self.constraints.function_type}")
        print(f"   📌 容积率: {self.constraints.plot_ratio}")
        print(f"   📌 建筑密度: {self.constraints.building_density}%")
        print(f"   📌 绿化率: {self.constraints.green_rate}%")
        print(f"   📌 限高: {self.constraints.height_limit}m")
        
        # 3. 场地分析
        print("\n🔍 步骤3: 场地条件分析...")
        self.site_analysis = analyze_site_conditions(self.boundary)
        
        print(f"   📐 用地形状: {self.site_analysis['shape_type']}")
        print(f"   📐 长宽比: {self.site_analysis['aspect_ratio']:.2f}")
        print(f"   📐 不规则度: {self.site_analysis['irregularity']:.2f}")
        
        # 4. 验证限制条件
        print("\n✅ 步骤4: 验证限制条件可行性...")
        validation = validate_constraints(self.constraints, self.boundary)
        
        if validation['valid']:
            print(f"   ✅ 所有限制条件可行")
        else:
            print(f"   ⚠️  警告: {', '.join(validation['messages'])}")
        
        if validation['suggestions']:
            print(f"   💡 建议: {', '.join(validation['suggestions'])}")
        
        print(f"   📊 理论最大建筑面积: {validation['max_building_area']:.2f} ㎡")
    
    def generate_design(self):
        """生成设计方案"""
        print(f"\n{'='*60}")
        print("🎨 步骤5: AI生成设计方案...")
        print(f"{'='*60}\n")
        
        # 生成功能分区
        print("📍 生成功能分区...")
        self.zones = generate_functional_zones(self.constraints, self.boundary)
        
        print(f"   共生成 {len(self.zones)} 个功能分区:")
        for zone in self.zones:
            print(f"   - {zone['name']}: {zone['area_ratio']*100:.1f}% ({zone['area']:.0f}㎡)")
        
        # 生成AI提示词（用于后续调用AI生成设计理念）
        print("\n🤖 生成AI设计提示词...")
        prompt = generate_design_prompt(self.constraints, self.boundary, self.site_analysis)
        
        # 保存提示词到文件
        prompt_file = os.path.join(self.output_dir, "ai_prompt.txt")
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        print(f"   ✅ AI提示词已保存: {prompt_file}")
        
        # 模拟设计理念（实际项目中应调用AI API生成）
        self.design_concept = {
            "theme": f"{'水墨江南' if '文旅' in self.constraints.function_type else '现代社区'} · {self.constraints.function_type}",
            "philosophy": f"本方案以{self.constraints.function_type}为核心，融合地域文化特色，打造集居住、休闲、文化体验于一体的综合性社区。通过合理的空间布局和景观设计，创造宜居、宜游、宜业的高品质生活环境。",
            "spatial_structure": "一核、两轴、多组团的空间结构。以中央景观为核心，组织主要功能分区。",
            "functional_layout": "根据用地特点，将功能分为核心展示区、商业休闲区、住宿度假区、景观游憩区和配套服务区五大板块。",
            "landscape_strategy": "以水景为脉络，串联各功能区。打造多层次的绿化系统，营造步移景异的景观体验。",
            "building_form": "采用现代中式建筑风格，体现地域文化特色。建筑高度控制在限高范围内，形成丰富的天际线。"
        }
        
        print(f"   ✅ 设计理念已生成")
        print(f"   📝 设计主题: {self.design_concept['theme']}")
    
    def generate_outputs(self):
        """生成所有输出成果"""
        print(f"\n{'='*60}")
        print("🖼️  步骤6: 生成设计成果...")
        print(f"{'='*60}\n")
        
        # 1. 彩色平面图
        print("🎨 生成彩色平面图...")
        plan_path = generate_colored_plan(
            self.boundary.points,
            self.zones,
            os.path.join(self.output_dir, "colored_plan.png")
        )
        
        # 2. 鸟瞰图
        print("\n🎨 生成鸟瞰效果图...")
        bird_path = generate_bird_eye_view(
            self.boundary.points,
            self.zones,
            os.path.join(self.output_dir, "bird_eye_view.png")
        )
        
        # 3. 分析图
        print("\n🎨 生成设计分析图...")
        analysis_paths = generate_analysis_diagrams(
            self.boundary.points,
            self.zones,
            os.path.join(self.output_dir, "analysis")
        )
        
        # 4. 设计说明文档
        print("\n📝 生成设计说明文档...")
        design_doc = generate_design_logic_text(self.design_concept, self.zones)
        doc_path = os.path.join(self.output_dir, "design_document.md")
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(design_doc)
        print(f"   ✅ 设计文档已保存: {doc_path}")
        
        # 5. 项目信息JSON
        print("\n💾 保存项目信息...")
        project_info = {
            "project_name": self.project_name,
            "created_at": datetime.now().isoformat(),
            "constraints": {
                "plot_ratio": self.constraints.plot_ratio,
                "building_density": self.constraints.building_density,
                "green_rate": self.constraints.green_rate,
                "height_limit": self.constraints.height_limit,
                "function_type": self.constraints.function_type
            },
            "site_info": {
                "area": self.boundary.area,
                "perimeter": self.boundary.boundary_length,
                "shape_type": self.site_analysis['shape_type']
            },
            "zones": self.zones,
            "outputs": {
                "colored_plan": plan_path,
                "bird_eye_view": bird_path,
                "analysis_diagrams": analysis_paths,
                "design_document": doc_path
            }
        }
        
        info_path = os.path.join(self.output_dir, "project_info.json")
        with open(info_path, 'w', encoding='utf-8') as f:
            json.dump(project_info, f, ensure_ascii=False, indent=2)
        print(f"   ✅ 项目信息已保存: {info_path}")
    
    def run(self, cad_file_path: str = "", constraints_dict: dict = None):
        """
        运行完整设计流程
        
        Args:
            cad_file_path: CAD文件路径（为空则使用示例数据）
            constraints_dict: 限制条件字典
        """
        # 默认参数
        if constraints_dict is None:
            constraints_dict = {
                'plot_ratio': 1.5,
                'building_density': 35.0,
                'green_rate': 30.0,
                'height_limit': 24.0,
                'function_type': '文旅小镇'
            }
        
        # 如果没有提供CAD文件，使用示例
        if not cad_file_path or not os.path.exists(cad_file_path):
            cad_file_path = "sample.dxf"
        
        # 执行设计流程
        self.load_project(cad_file_path, constraints_dict)
        self.generate_design()
        self.generate_outputs()
        
        # 完成报告
        print(f"\n{'='*60}")
        print("✅ 设计方案生成完成！")
        print(f"{'='*60}\n")
        
        print(f"📁 所有成果已保存到: {os.path.abspath(self.output_dir)}/")
        print("\n🎨 生成的文件:")
        print(f"   1. colored_plan.png - 彩色总平面图")
        print(f"   2. bird_eye_view.png - 鸟瞰效果图")
        print(f"   3. analysis/zoning_analysis.png - 功能分区分析图")
        print(f"   4. analysis/area_distribution.png - 面积分配图")
        print(f"   5. design_document.md - 设计说明文档")
        print(f"   6. ai_prompt.txt - AI设计提示词")
        print(f"   7. project_info.json - 项目信息")
        
        print(f"\n🚀 打开 frontend/index.html 查看Web界面")

def main():
    """主函数"""
    # 创建AI设计助手实例
    ai_designer = UrbanDesignAI()
    
    # 获取用户输入（简化版，实际应有交互界面）
    print("\n🏙️  UrbanDesignAI - AI城市规划设计助手")
    print("=" * 60)
    print("\n请输入项目参数（直接回车使用默认值）:\n")
    
    try:
        function_type = input("功能定位 [文旅小镇]: ").strip() or "文旅小镇"
        plot_ratio = float(input("容积率 [1.5]: ").strip() or "1.5")
        building_density = float(input("建筑密度% [35]: ").strip() or "35")
        green_rate = float(input("绿化率% [30]: ").strip() or "30")
        height_limit = float(input("限高(米) [24]: ").strip() or "24")
        
        constraints = {
            'function_type': function_type,
            'plot_ratio': plot_ratio,
            'building_density': building_density,
            'green_rate': green_rate,
            'height_limit': height_limit
        }
        
        # 运行设计流程
        ai_designer.run("", constraints)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  程序被中断")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
