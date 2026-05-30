#!/bin/bash

# Typora 图片上传脚本
# 此脚本用于将图片上传到 GitHub 仓库并返回可访问的链接

# 配置变量
REPO_PATH="/path/to/your/Typora-image"  # 修改为你的仓库路径
GITHUB_USERNAME="YaoXingjin"             # 修改为你的 GitHub 用户名
REPO_NAME="Typora-image"                 # 仓库名称

# 获取当前日期
YEAR=$(date +%Y)
MONTH=$(date +%m)

# 创建目标目录
TARGET_DIR="$REPO_PATH/images/$YEAR/$MONTH"
mkdir -p "$TARGET_DIR"

# 处理上传的图片
for image in "$@"; do
    if [ -f "$image" ]; then
        # 获取文件扩展名
        extension="${image##*.}"
        
        # 生成唯一文件名（时间戳 + 随机数）
        timestamp=$(date +%Y%m%d_%H%M%S)
        random=$(shuf -i 1000-9999 -n 1)
        filename="${timestamp}_${random}.${extension}"
        
        # 复制文件到目标目录
        cp "$image" "$TARGET_DIR/$filename"
        
        # 切换到仓库目录
        cd "$REPO_PATH"
        
        # 添加、提交并推送文件
        git add "images/$YEAR/$MONTH/$filename"
        git commit -m "Add image: $filename"
        git push origin main
        
        # 生成 GitHub 链接并输出
        github_url="https://raw.githubusercontent.com/$GITHUB_USERNAME/$REPO_NAME/main/images/$YEAR/$MONTH/$filename"
        echo "$github_url"
    fi
done