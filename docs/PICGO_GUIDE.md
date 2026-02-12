# PicGo 配置指南

PicGo 是一个功能强大的图片上传工具，支持多种图床服务。本指南将详细介绍如何配置 PicGo 与此 GitHub 仓库配合使用。

## 📦 安装 PicGo

### 下载地址
- 官方网站：https://molunerfinn.com/PicGo/
- GitHub 地址：https://github.com/Molunerfinn/PicGo/releases

### 支持平台
- Windows 10/11
- macOS 10.12+
- Linux（AppImage 格式）

## ⚙️ 详细配置步骤

### 1. 获取 GitHub Personal Access Token

1. 登录 GitHub，访问 [Personal Access Tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 填写 Token 信息：
   - **Note**: `PicGo-Typora-image`（或任何你喜欢的名称）
   - **Expiration**: 建议选择 "No expiration"（无期限）
   - **Scopes**: 勾选 `repo`（完整的仓库权限）
4. 点击 "Generate token"
5. **重要**：立即复制生成的 token（这是唯一一次显示）

### 2. 配置 PicGo GitHub 图床

1. 打开 PicGo 应用
2. 在左侧导航栏选择 "图床设置"
3. 选择 "GitHub图床"
4. 填写以下配置：

```
仓库名: YaoXingjin/Typora-image
分支名: main
Token: [粘贴你刚才复制的 GitHub Token]
存储路径: images/{year}/{month}/
自定义域名: https://raw.githubusercontent.com/YaoXingjin/Typora-image/main
```

#### 配置说明：

- **仓库名**: 格式为 `用户名/仓库名`
- **分支名**: 通常是 `main`，部分旧仓库可能是 `master`
- **Token**: 刚才获取的 GitHub Personal Access Token
- **存储路径**: 
  - `images/{year}/{month}/` 会自动按年月分类
  - 也可以使用 `images/` 或其他自定义路径
- **自定义域名**: 使用 GitHub Raw 地址确保图片可直接访问

### 3. 配置 Typora

#### 方法一：自动检测（推荐）

1. 打开 Typora 偏好设置（`Ctrl/Cmd + ,`）
2. 选择 "图像" 选项卡
3. 在 "插入图片时" 选择 "上传图片"
4. "上传服务设置" 选择 "PicGo(app)"
5. PicGo 路径通常会自动检测，如果没有，请手动选择 PicGo 安装路径

#### 方法二：手动指定路径

如果自动检测失败，需要手动指定 PicGo 路径：

**Windows:**
```
C:\Users\你的用户名\AppData\Local\Programs\PicGo\PicGo.exe
```

**macOS:**
```
/Applications/PicGo.app/Contents/MacOS/PicGo
```

**Linux:**
```
/opt/PicGo/picgo
```

### 4. 测试配置

1. 在 Typora 中插入一张图片（拖拽或复制粘贴）
2. 观察 PicGo 是否弹出上传通知
3. 检查图片是否成功显示
4. 验证 GitHub 仓库中是否添加了图片文件

## 🎨 高级配置

### 时间戳命名

在 PicGo 的 "PicGo设置" → "时间戳重命名" 中可以启用：
- 自动重命名避免文件冲突
- 格式：`YYYYMMDD-HHmmss-随机数.ext`

### 图片压缩

安装压缩插件可以减小图片大小：
1. 在 PicGo 中选择 "插件设置"
2. 搜索并安装 `picgo-plugin-compress`
3. 配置压缩参数

### 快捷上传

配置快捷键实现快速截图上传：
1. 在 "PicGo设置" → "快捷键设置" 中配置
2. 推荐快捷键：`Ctrl+Shift+P`（Windows）或 `Cmd+Shift+P`（macOS）

## 🔧 故障排除

### 常见问题

#### 1. 上传失败：Token 无效
- 检查 Token 是否正确复制
- 确认 Token 权限包含 `repo`
- 重新生成 Token 并更新配置

#### 2. 图片无法显示
- 确认仓库是公开的（Private 仓库图片无法直接访问）
- 检查自定义域名配置是否正确
- 验证文件确实上传到了 GitHub

#### 3. Typora 找不到 PicGo
- 检查 PicGo 是否正确安装
- 手动指定 PicGo 可执行文件路径
- 确保 PicGo 应用可以正常启动

#### 4. 网络连接问题
- 检查网络连接是否正常
- 如果在国内，可能需要配置代理
- 尝试使用其他网络环境

### 日志查看

如果遇到问题，可以查看 PicGo 日志：
1. 在 PicGo 主界面点击 "设置" → "设置日志文件"
2. 查看详细的错误信息
3. 根据错误信息进行相应的调整

## 📋 配置检查清单

使用前请确认以下项目：

- [ ] GitHub Personal Access Token 已获取且权限正确
- [ ] PicGo 中 GitHub 图床配置完整
- [ ] 仓库名称格式正确（用户名/仓库名）
- [ ] 仓库是公开的
- [ ] Typora 中已正确配置 PicGo 路径
- [ ] 网络连接正常，能访问 GitHub
- [ ] 测试上传一张图片确认功能正常

## 🔄 备份与恢复

### 导出配置

定期备份 PicGo 配置：
1. 在 PicGo 设置中选择 "导出配置"
2. 保存配置文件到安全位置

### 导入配置

在新设备上恢复配置：
1. 安装 PicGo
2. 选择 "导入配置"
3. 导入之前备份的配置文件

通过以上配置，你就可以愉快地使用 PicGo + GitHub 作为 Typora 的图床服务了！