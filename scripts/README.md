# Typora 图床配置说明

## 配置步骤

### 1. 克隆仓库到本地

```bash
git clone https://github.com/YaoXingjin/Typora-image.git
cd Typora-image
```

### 2. 修改上传脚本

编辑 `scripts/upload.sh` 文件，修改以下配置：

```bash
REPO_PATH="/path/to/your/Typora-image"  # 修改为你的仓库本地路径
GITHUB_USERNAME="YaoXingjin"             # 修改为你的 GitHub 用户名
REPO_NAME="Typora-image"                 # 仓库名称
```

### 3. 在 Typora 中配置

1. 打开 Typora
2. 进入 `偏好设置` → `图像`
3. 选择 `插入图片时` → `上传图片`
4. 选择 `上传服务设置` → `自定义命令`
5. 在命令框中输入：

**Windows:**
```bash
bash /path/to/your/Typora-image/scripts/upload.sh
```

**macOS/Linux:**
```bash
/path/to/your/Typora-image/scripts/upload.sh
```

### 4. 测试配置

1. 在 Typora 中插入一张图片
2. 检查是否自动上传并生成链接
3. 验证链接是否可以正常访问

## 注意事项

- 确保已配置 Git 的用户名和邮箱
- 确保有推送到仓库的权限
- 建议使用 SSH 密钥进行 Git 认证
- 仓库必须是公开的，否则图片链接无法访问

## 故障排除

### 上传失败
- 检查网络连接
- 验证 Git 配置和权限
- 确认脚本路径正确

### 链接无法访问
- 确认仓库是公开的
- 检查文件是否成功上传到 GitHub
- 验证链接格式是否正确