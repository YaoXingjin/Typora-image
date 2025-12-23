# PicGo vs 自定义脚本：选择指南

既然你已经下载了 PicGo，这里为你详细对比两种方案，帮助你选择最适合的图床上传方式。

## 📊 功能对比

| 特性 | PicGo | 自定义脚本 |
|------|-------|------------|
| **易用性** | ⭐⭐⭐⭐⭐ 图形界面，配置简单 | ⭐⭐⭐ 需要修改配置文件 |
| **稳定性** | ⭐⭐⭐⭐ 成熟软件，更新频繁 | ⭐⭐⭐ 简单脚本，相对稳定 |
| **功能丰富** | ⭐⭐⭐⭐⭐ 支持多种图床，插件系统 | ⭐⭐ 专为此仓库设计 |
| **自定义性** | ⭐⭐⭐ 通过插件扩展 | ⭐⭐⭐⭐⭐ 完全可控，可随意修改 |
| **跨平台** | ⭐⭐⭐⭐⭐ Windows/macOS/Linux | ⭐⭐⭐⭐ 需要 Bash 或 Python 环境 |
| **文件管理** | ⭐⭐⭐ 依赖图床服务 | ⭐⭐⭐⭐⭐ 完全掌控文件组织 |
| **离线使用** | ❌ 需要网络连接 | ✅ 本地操作后上传 |
| **学习成本** | ⭐⭐ 很低 | ⭐⭐⭐⭐ 需要了解脚本配置 |

## 🎯 推荐选择

### 选择 PicGo 如果你：

✅ **新手用户或追求简单**
- 不想手动配置脚本
- 希望有图形化界面
- 想要即开即用的体验

✅ **需要多图床支持**
- 同时使用多个图床服务
- 希望在不同图床间切换
- 需要图床的高级功能（如图片压缩、水印等）

✅ **团队协作**
- 多人使用相同配置
- 需要标准化的上传流程
- 希望减少技术门槛

### 选择自定义脚本如果你：

✅ **技术用户或追求控制**
- 希望完全掌控文件存储
- 需要自定义文件命名和目录结构
- 想要了解上传过程的每个步骤

✅ **隐私和安全考虑**
- 不信任第三方图床服务
- 希望图片完全存储在自己的仓库
- 需要离线编辑功能

✅ **特殊需求**
- 需要特定的文件组织方式
- 要集成到其他自动化流程
- 希望扩展脚本功能

## 🚀 快速配置指南

### 方案一：使用 PicGo（推荐新手）

#### 1. 配置 GitHub 图床

1. 打开 PicGo 应用
2. 在左侧选择"图床设置" → "GitHub图床"
3. 填写配置信息：
   ```
   仓库名：YaoXingjin/Typora-image
   分支名：main
   Token：[你的 GitHub Personal Access Token]
   存储路径：images/{year}/{month}/
   自定义域名：https://raw.githubusercontent.com/YaoXingjin/Typora-image/main
   ```

#### 2. 获取 GitHub Token

1. 访问 [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token"
3. 勾选 `repo` 权限
4. 复制生成的 token 并填入 PicGo

#### 3. 配置 Typora

1. 打开 Typora 偏好设置
2. 选择 "图像" 选项卡
3. 设置上传服务为 "PicGo(app)"
4. 如果需要，设置 PicGo 路径

### 方案二：使用自定义脚本（推荐技术用户）

#### 1. 选择脚本类型

**Python 脚本（推荐，跨平台）：**
```bash
# Windows
python /path/to/Typora-image/scripts/upload.py

# macOS/Linux  
python3 /path/to/Typora-image/scripts/upload.py
```

**Bash 脚本（Linux/macOS）：**
```bash
/path/to/Typora-image/scripts/upload.sh
```

#### 2. 修改脚本配置

编辑 `scripts/upload.py` 或 `scripts/upload.sh`：

```python
# Python 脚本配置
REPO_PATH = "/Users/你的用户名/Typora-image"  # 改为实际路径
GITHUB_USERNAME = "YaoXingjin"  # 改为你的用户名
REPO_NAME = "Typora-image"
```

#### 3. 配置 Typora

在 Typora 的图像设置中选择"自定义命令"，填入对应的脚本路径。

## 💡 最佳实践建议

### 如果选择 PicGo：

1. **定期备份配置**：导出 PicGo 配置文件
2. **使用插件**：安装 `picgo-plugin-github-plus` 获得更多功能
3. **设置快捷键**：配置截图上传快捷键提高效率
4. **配置压缩**：启用图片压缩节省空间

### 如果选择自定义脚本：

1. **版本控制**：将脚本也加入版本控制
2. **错误处理**：增强脚本的错误处理和日志记录
3. **自动化**：可以添加图片压缩、格式转换等功能
4. **监控**：定期检查上传是否成功

## 🔄 迁移指南

### 从自定义脚本迁移到 PicGo：

1. 备份现有图片文件
2. 按照上方指南配置 PicGo
3. 测试上传功能
4. 更新 Typora 配置

### 从 PicGo 迁移到自定义脚本：

1. 导出 PicGo 中的图片链接列表
2. 下载配置自定义脚本
3. 批量测试脚本功能
4. 更新 Typora 配置

## 📈 总结

- **新手或追求简单**：选择 PicGo
- **技术用户或需要完全控制**：选择自定义脚本
- **团队使用**：PicGo 更适合标准化
- **个人使用且重视隐私**：自定义脚本更合适

两种方案都能很好地满足 Typora 图床需求，选择最适合你的使用习惯和技术水平的方案即可。