#!/usr/bin/env python3
"""
DeepSeek批量学习系统 V1.0
使用新API Key开始自动化学习
"""

import requests
import json
import os
from datetime import datetime

API_KEY = "sk-d55324c1bd464b4daee34ec09c027993"
BASE_URL = "https://api.deepseek.com/v1"

def ask_deepseek(question, system_prompt="你是一个专业的建筑设计和文旅规划专家。", max_retries=3):
    """向DeepSeek提问，带重试机制"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7,
        "max_tokens": 1500
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                f"{BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.Timeout:
            print(f"    ⚠️ 超时，重试 {attempt+1}/{max_retries}...")
            if attempt == max_retries - 1:
                return "Error: 请求超时，请稍后重试"
        except Exception as e:
            print(f"    ❌ 错误: {str(e)[:50]}")
            if attempt == max_retries - 1:
                return f"Error: {str(e)}"
    
    return "Error: 达到最大重试次数"

def batch_learning():
    """批量学习任务 - Day 1冲刺"""
    
    print("🚀 DeepSeek批量学习系统启动！")
    print("目标：今日学习50个知识点")
    print("=" * 60)
    
    # 学习主题列表
    topics = [
        {
            "agent": "城市设计专家",
            "topic": "滨水文旅小镇规划",
            "questions": [
                "全球最著名的10个滨水文旅小镇案例有哪些？它们的规划亮点是什么？",
                "滨水小镇的空间结构通常有哪些模式？各自的优缺点？",
                "如何处理滨水小镇的水岸线和建筑退界？",
            ]
        },
        {
            "agent": "建筑设计专家",
            "topic": "文旅酒店建筑设计",
            "questions": [
                "全球获奖的精品酒店建筑设计案例有哪些？设计亮点？",
                "度假酒店设计中如何处理与自然景观的关系？",
                "如何在现代建筑中融入地域文化元素？",
            ]
        },
        {
            "agent": "投资金融专家",
            "topic": "文旅项目投资分析",
            "questions": [
                "文旅项目投资测算的关键指标有哪些？如何计算？",
                "成功的文旅项目融资模式有哪些案例？",
                "如何评估文旅项目的投资回报周期？",
            ]
        },
        {
            "agent": "文旅运营专家",
            "topic": "文旅项目运营策略",
            "questions": [
                "全球运营最成功的文旅项目有哪些？它们的运营秘诀？",
                "如何设计文旅项目的游客动线和停留时间？",
                "文旅项目的收入来源通常有哪些比例构成？",
            ]
        },
        {
            "agent": "文化策划专家",
            "topic": "文旅IP打造",
            "questions": [
                "最成功的文旅IP案例有哪些？它们是如何打造的？",
                "如何将地域文化转化为可体验的产品？",
                "文旅项目的故事线如何设计？",
            ]
        },
    ]
    
    # 保存结果
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    os.makedirs("learning/deepseek", exist_ok=True)
    
    all_results = []
    
    for topic_info in topics:
        agent = topic_info["agent"]
        topic = topic_info["topic"]
        
        print(f"\n📚 {agent} 正在学习: {topic}")
        print("-" * 60)
        
        agent_results = {
            "agent": agent,
            "topic": topic,
            "timestamp": datetime.now().isoformat(),
            "qa_pairs": []
        }
        
        for i, question in enumerate(topic_info["questions"], 1):
            print(f"  问题 {i}/{len(topic_info['questions'])}: {question[:50]}...")
            
            answer = ask_deepseek(
                question,
                f"你是{agent}，专注于{topic}。请提供详细的案例分析和实操建议。"
            )
            
            agent_results["qa_pairs"].append({
                "question": question,
                "answer": answer
            })
            
            print(f"  ✅ 完成 ({len(answer)} 字符)")
        
        all_results.append(agent_results)
        
        # 保存单个Agent的学习成果
        agent_file = f"learning/deepseek/{agent.replace(' ', '_')}_{timestamp}.json"
        with open(agent_file, "w", encoding="utf-8") as f:
            json.dump(agent_results, f, ensure_ascii=False, indent=2)
        print(f"  💾 已保存: {agent_file}")
    
    # 保存总结果
    summary_file = f"learning/deepseek/batch_learning_{timestamp}.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 60)
    print(f"✅ 批量学习完成！")
    print(f"📊 共学习: {len(topics)} 个主题, {sum(len(t['questions']) for t in topics)} 个问题")
    print(f"💾 保存位置: learning/deepseek/")
    print(f"📄 汇总文件: {summary_file}")
    
    return all_results

if __name__ == "__main__":
    results = batch_learning()
