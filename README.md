# Typora-image

这个仓库用作 Typora 的图床，用于存储和管理 Typora 中使用的图片。

## 快速开始

### 步骤 1：克隆仓库
```bash
git clone https://github.com/YaoXingjin/Typora-image.git
cd Typora-image
```

### 步骤 2：配置脚本
编辑 `scripts/upload.sh` 或 `scripts/upload.py`，修改其中的路径配置。

### 步骤 3：设置 Typora
在 Typora 的图像设置中配置自定义上传命令。

详细配置说明请参考 `scripts/README.md` 文件。

## 使用方法

### 1. 设置 Typora 图片上传

在 Typora 中进行以下设置：

1. 打开 Typora 偏好设置
2. 选择"图像"选项卡
3. 在"插入图片时"选择"上传图片"
4. 在"上传服务设置"中选择自定义命令
5. 配置上传命令（见下方配置示例）

### 2. 目录结构

```
Typora-image/
├── images/              # 图片存储目录
│   ├── 2024/           # 按年份分类
│   │   ├── 01/         # 按月份分类
│   │   └── 02/
│   └── temp/           # 临时图片
├── scripts/            # 上传脚本
└── README.md
```

### 3. 配置示例

#### 方案一：Bash 脚本（Linux/macOS 推荐）

```bash
# 在 Typora 自定义命令中使用：
/path/to/your/Typora-image/scripts/upload.sh
```

#### 方案二：Python 脚本（跨平台推荐）

```bash
# 在 Typora 自定义命令中使用：
python /path/to/your/Typora-image/scripts/upload.py
```

或者在 Windows 上：
```cmd
python C:\path\to\your\Typora-image\scripts\upload.py
```

### 4. 使用说明

1. 将图片拖拽到 Typora 中
2. Typora 会自动调用上传脚本
3. 图片会被上传到此仓库
4. 返回 GitHub 图片链接供 Typora 使用

### 5. 注意事项

- 确保仓库为公开仓库，以便图片链接可以正常访问
- 建议定期整理图片，按时间或主题分类
- 注意 GitHub 仓库大小限制

## 贡献

欢迎提交问题和建议来改进这个图床服务。