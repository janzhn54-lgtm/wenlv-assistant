#!/usr/bin/env python3
"""
文旅空间 CAD 自动生成 + AI 生图 Prompt 生成器
用于快速生成展厅/民宿/商业空间的平面方案
"""

import ezdxf
import json
from dataclasses import dataclass, asdict
from typing import List, Tuple
from pathlib import Path


@dataclass
class SpaceConfig:
    """空间配置参数"""
    space_type: str = "展厅"  # 展厅/民宿/商业
    width: float = 12.0      # 米
    depth: float = 8.0       # 米
    height: float = 3.5      # 层高
    entrance: str = "south"  # 入口方向
    style: str = "新中式"     # 风格
    
    # 功能分区
    has_reception: bool = True   # 接待区
    has_display: bool = True     # 展示区
    has_rest: bool = True        # 休息区
    has_office: bool = False     # 办公区
    
    # 环境参数
    natural_light: str = "良好"   # 采光条件
    target_audience: str = "游客" # 目标人群


class SpaceDesigner:
    """空间设计生成器"""
    
    def __init__(self, config: SpaceConfig):
        self.config = config
        self.doc = ezdxf.new("R2010")
        self.msp = self.doc.modelspace()
        self.zones = []  # 记录功能分区信息
        
    def generate(self) -> str:
        """生成 CAD 文件并返回路径"""
        self._draw_outer_walls()
        self._draw_entrance()
        self._draw_zones()
        self._add_dimensions()
        
        output_path = f"output/{self.config.space_type}_平面方案.dxf"
        Path(output_path).parent.mkdir(exist_ok=True)
        self.doc.saveas(output_path)
        return output_path
    
    def _draw_outer_walls(self):
        """绘制外墙"""
        w, d = self.config.width, self.config.depth
        # 外墙厚度 0.2m
        self.msp.add_lwpolyline([
            (0, 0), (w, 0), (w, d), (0, d), (0, 0)
        ], close=True)
        # 内墙线
        self.msp.add_lwpolyline([
            (0.2, 0.2), (w-0.2, 0.2), (w-0.2, d-0.2), (0.2, d-0.2), (0.2, 0.2)
        ], close=True)
        
    def _draw_entrance(self):
        """绘制入口"""
        w = self.config.width
        # 默认南侧入口，宽 1.5m
        if self.config.entrance == "south":
            self.msp.add_line((w/2 - 0.75, 0), (w/2 + 0.75, 0))
            self.zones.append({"name": "入口", "pos": (w/2, 0), "area": 0})
            
    def _draw_zones(self):
        """绘制功能分区"""
        w, d = self.config.width, self.config.depth
        current_x = 1.0
        
        if self.config.has_reception:
            # 接待区：入口附近，宽 3m
            zone_w = 3.0
            self._draw_zone(current_x, 0.5, zone_w, 2.5, "接待区", (1, 0.5, 0.5))
            current_x += zone_w + 0.5
            
        if self.config.has_display:
            # 展示区：主体空间
            zone_w = w - current_x - 1.5
            self._draw_zone(current_x, 0.5, zone_w, d - 1.5, "展示区", (0.5, 0.7, 0.9))
            
        if self.config.has_rest:
            # 休息区：角落
            self._draw_zone(w - 2.5, d - 2.0, 2.0, 1.5, "休息区", (0.6, 0.9, 0.6))
            
    def _draw_zone(self, x: float, y: float, w: float, h: float, 
                   name: str, color: Tuple[float, float, float]):
        """绘制单个功能区"""
        # 区域框
        self.msp.add_lwpolyline([
            (x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)
        ], close=True)
        # 文字标注
        text = self.msp.add_text(name, height=0.3, dxfattribs={"layer": "标注"})
        text.set_placement((x + w/2, y + h/2), align=ezdxf.enums.TextEntityAlignment.MIDDLE_CENTER)
        # 记录分区信息
        self.zones.append({
            "name": name,
            "position": (round(x, 2), round(y, 2)),
            "size": (round(w, 2), round(h, 2)),
            "area": round(w * h, 2)
        })
        
    def _add_dimensions(self):
        """添加尺寸标注"""
        # 简化版：在角落添加总面积文字
        text = self.msp.add_text(
            f"总面积: {self.config.width * self.config.depth:.1f}㎡", 
            height=0.25
        )
        text.set_placement((0.5, self.config.depth + 0.3))


class PromptGenerator:
    """AI 生图 Prompt 生成器"""
    
    STYLE_PROMPTS = {
        "新中式": "New Chinese style, minimalist wooden furniture, white walls with ink wash accents, ",
        "宋韵": "Song Dynasty aesthetic, elegant simplicity, natural materials, muted earth tones, ",
        "工业风": "Industrial loft style, exposed brick and steel, vintage lighting, ",
        "北欧": "Scandinavian design, light wood, white and grey palette, cozy hygge atmosphere, ",
        "日式": "Japanese wabi-sabi, natural wood, paper screens, zen garden elements, "
    }
    
    SPACE_TYPE_PROMPTS = {
        "展厅": "cultural exhibition hall, display shelves, informational panels, visitors viewing exhibits, ",
        "民宿": "boutique guesthouse, cozy bedroom, traditional courtyard, hospitality space, ",
        "商业": "retail store, product displays, customer browsing, modern commercial interior, "
    }
    
    def __init__(self, config: SpaceConfig, zones: List[dict]):
        self.config = config
        self.zones = zones
        
    def generate(self) -> dict:
        """生成完整的 Prompt 信息"""
        base_prompt = self._build_base_prompt()
        negative_prompt = "cluttered, messy, dark, outdated, cheap materials, distorted perspective"
        
        return {
            "project_info": asdict(self.config),
            "zones": self.zones,
            "prompts": {
                "main": base_prompt,
                "negative": negative_prompt,
                "variations": self._generate_variations()
            },
            "parameters": {
                "aspect_ratio": "16:9",
                "style_preset": "Architectural Photography",
                "quality_tags": "8k, photorealistic, architectural visualization, professional photography"
            }
        }
    
    def _build_base_prompt(self) -> str:
        """构建主 Prompt"""
        parts = []
        
        # 空间类型
        space_desc = self.SPACE_TYPE_PROMPTS.get(
            self.config.space_type, 
            f"{self.config.space_type} interior"
        )
        parts.append(space_desc)
        
        # 尺寸信息
        parts.append(f"{self.config.width * self.config.depth:.0f}sqm space, ")
        parts.append(f"{self.config.height}m ceiling height, ")
        
        # 风格
        style_desc = self.STYLE_PROMPTS.get(self.config.style, f"{self.config.style} design, ")
        parts.append(style_desc)
        
        # 功能分区
        zone_names = [z["name"] for z in self.zones if z.get("area", 0) > 0]
        if zone_names:
            parts.append(f"functional zones including {', '.join(zone_names)}, ")
        
        # 环境
        parts.append(f"{self.config.natural_light.lower()} natural lighting, ")
        
        # 收尾
        parts.append("clean lines, professional interior design, warm atmosphere")
        
        return "".join(parts)
    
    def _generate_variations(self) -> List[dict]:
        """生成多个风格的变体"""
        variations = []
        
        for style_name, style_prompt in self.STYLE_PROMPTS.items():
            if style_name != self.config.style:
                base = self._build_base_prompt()
                # 替换风格部分
                original_style = self.STYLE_PROMPTS.get(self.config.style, "")
                new_prompt = base.replace(original_style, style_prompt)
                variations.append({
                    "style": style_name,
                    "prompt": new_prompt
                })
        
        return variations[:3]  # 返回3个变体


def main():
    """主流程"""
    print("🏛️  文旅空间自动生成器\n")
    
    # 1. 配置参数
    config = SpaceConfig(
        space_type="展厅",
        width=15,
        depth=10,
        height=4.0,
        style="宋韵",
        has_reception=True,
        has_display=True,
        has_rest=True,
        natural_light="优秀"
    )
    
    print(f"📐 生成 {config.space_type} 方案...")
    print(f"   尺寸: {config.width}m × {config.depth}m")
    print(f"   风格: {config.style}\n")
    
    # 2. 生成 CAD
    designer = SpaceDesigner(config)
    cad_path = designer.generate()
    print(f"✅ CAD 已保存: {cad_path}")
    
    # 3. 生成 Prompt
    prompt_gen = PromptGenerator(config, designer.zones)
    prompts = prompt_gen.generate()
    
    # 4. 保存 Prompt
    prompt_path = f"output/{config.space_type}_prompts.json"
    with open(prompt_path, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"✅ Prompt 已保存: {prompt_path}\n")
    
    # 5. 显示结果
    print("🎨 主 Prompt:")
    print("-" * 60)
    print(prompts["prompts"]["main"])
    print("-" * 60)
    
    print(f"\n📋 功能分区:")
    for zone in prompts["zones"]:
        if zone.get("area", 0) > 0:
            print(f"   • {zone['name']}: {zone['size'][0]}m × {zone['size'][1]}m = {zone['area']}㎡")
    
    print(f"\n🔄 风格变体 ({len(prompts['prompts']['variations'])} 个):")
    for v in prompts["prompts"]["variations"]:
        print(f"   • {v['style']}")
    
    print("\n💡 使用建议:")
    print("   1. 用 CAD 软件打开 .dxf 文件查看平面")
    print("   2. 将 prompt 粘贴到 Midjourney/Stable Diffusion")
    print("   3. 添加 --ar 16:9 参数生成宽图")
    print("   4. 用变体 prompt 快速生成多套风格方案")


if __name__ == "__main__":
    main()
