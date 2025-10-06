#!/usr/bin/env python3
"""
验证配置脚本 - 检查 PicGo 和自定义脚本的配置是否正确
"""

import os
import sys
from pathlib import Path

def validate_repository_structure():
    """验证仓库结构"""
    print("🔍 检查仓库结构...")
    
    # 检查必要的目录和文件
    required_items = [
        "README.md",
        "docs/COMPARISON.md", 
        "docs/PICGO_GUIDE.md",
        "docs/QUICK_DECISION.md",
        "ANSWER.md"
    ]
    
    missing_items = []
    for item in required_items:
        if not Path(item).exists():
            missing_items.append(item)
    
    if missing_items:
        print(f"❌ 缺少文件/目录: {missing_items}")
        return False
    else:
        print("✅ 仓库结构完整")
        return True

def validate_picgo_config():
    """验证 PicGo 推荐配置"""
    print("\n🔍 检查 PicGo 配置建议...")
    
    # 检查配置指南是否包含必要信息
    guide_path = Path("docs/PICGO_GUIDE.md")
    if not guide_path.exists():
        print("❌ PicGo 配置指南不存在")
        return False
    
    content = guide_path.read_text(encoding='utf-8')
    required_sections = [
        "YaoXingjin/Typora-image",  # 仓库名
        "main",  # 分支名
        "images/{year}/{month}/",  # 存储路径
        "https://raw.githubusercontent.com",  # 自定义域名
        "GitHub Personal Access Token"  # Token 说明
    ]
    
    missing_sections = []
    for section in required_sections:
        if section not in content:
            missing_sections.append(section)
    
    if missing_sections:
        print(f"❌ 配置指南缺少: {missing_sections}")
        return False
    else:
        print("✅ PicGo 配置指南完整")
        return True

def validate_comparison():
    """验证对比文档"""
    print("\n🔍 检查对比文档...")
    
    comparison_path = Path("docs/COMPARISON.md")
    if not comparison_path.exists():
        print("❌ 对比文档不存在")
        return False
    
    content = comparison_path.read_text(encoding='utf-8')
    required_content = [
        "易用性",
        "稳定性", 
        "功能丰富",
        "自定义性",
        "新手用户",
        "技术用户"
    ]
    
    missing_content = []
    for item in required_content:
        if item not in content:
            missing_content.append(item)
    
    if missing_content:
        print(f"❌ 对比文档缺少: {missing_content}")
        return False
    else:
        print("✅ 对比文档完整")
        return True

def validate_answer():
    """验证直接回答文档"""
    print("\n🔍 检查直接回答...")
    
    answer_path = Path("ANSWER.md")
    if not answer_path.exists():
        print("❌ 直接回答文档不存在")
        return False
    
    content = answer_path.read_text(encoding='utf-8')
    if "建议你优先使用 PicGo" not in content:
        print("❌ 没有明确推荐")
        return False
    
    print("✅ 直接回答文档完整")
    return True

def main():
    """主验证函数"""
    print("🚀 开始验证配置...")
    
    checks = [
        validate_repository_structure(),
        validate_picgo_config(),
        validate_comparison(),
        validate_answer()
    ]
    
    if all(checks):
        print("\n🎉 所有验证通过！配置文档已准备就绪。")
        print("\n📋 用户可以：")
        print("1. 阅读 ANSWER.md 获得直接建议")
        print("2. 使用 docs/QUICK_DECISION.md 快速决策") 
        print("3. 查看 docs/COMPARISON.md 了解详细对比")
        print("4. 跟随 docs/PICGO_GUIDE.md 配置 PicGo")
        return True
    else:
        print("\n❌ 验证失败，请检查缺少的文件或内容")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)