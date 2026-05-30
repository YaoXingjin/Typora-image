#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Typora 图片上传脚本 (Python 版本)
支持跨平台使用，比 bash 脚本更稳定
"""

import os
import sys
import shutil
import subprocess
import datetime
import random
from pathlib import Path

# 配置变量 - 请根据实际情况修改
REPO_PATH = "/path/to/your/Typora-image"  # 修改为你的仓库路径
GITHUB_USERNAME = "YaoXingjin"             # 修改为你的 GitHub 用户名
REPO_NAME = "Typora-image"                 # 仓库名称

def upload_image(image_path):
    """上传单个图片文件"""
    if not os.path.isfile(image_path):
        print(f"错误: 文件不存在 {image_path}", file=sys.stderr)
        return None
    
    # 获取当前日期
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    
    # 创建目标目录
    target_dir = Path(REPO_PATH) / "images" / year / month
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成唯一文件名
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    random_num = random.randint(1000, 9999)
    file_extension = Path(image_path).suffix
    filename = f"{timestamp}_{random_num}{file_extension}"
    
    # 复制文件到目标目录
    target_path = target_dir / filename
    try:
        shutil.copy2(image_path, target_path)
    except Exception as e:
        print(f"错误: 复制文件失败 {e}", file=sys.stderr)
        return None
    
    # Git 操作
    try:
        os.chdir(REPO_PATH)
        
        # 添加文件
        subprocess.run(["git", "add", f"images/{year}/{month}/{filename}"], 
                      check=True, capture_output=True)
        
        # 提交
        subprocess.run(["git", "commit", "-m", f"Add image: {filename}"], 
                      check=True, capture_output=True)
        
        # 推送
        subprocess.run(["git", "push", "origin", "main"], 
                      check=True, capture_output=True)
        
    except subprocess.CalledProcessError as e:
        print(f"错误: Git 操作失败 {e}", file=sys.stderr)
        return None
    
    # 生成 GitHub 链接
    github_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/images/{year}/{month}/{filename}"
    return github_url

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python upload.py <图片文件1> [图片文件2] ...", file=sys.stderr)
        sys.exit(1)
    
    # 处理所有传入的图片文件
    for image_path in sys.argv[1:]:
        url = upload_image(image_path)
        if url:
            print(url)
        else:
            print(f"上传失败: {image_path}", file=sys.stderr)

if __name__ == "__main__":
    main()