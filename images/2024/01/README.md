# 示例图片

这是一个示例图片目录，展示了图片存储的结构。

实际使用时，上传的图片会按照以下规则存储：

- **文件名格式**: `YYYYMMDD_HHMMSS_XXXX.ext`
  - `YYYYMMDD`: 上传日期
  - `HHMMSS`: 上传时间  
  - `XXXX`: 4位随机数
  - `ext`: 文件扩展名

- **目录结构**: `images/YYYY/MM/`
  - 按年份和月份分类存储
  - 便于管理和查找

## 使用示例

当你在 Typora 中插入图片时，图片会被自动上传到这里，并生成如下格式的链接：

```
https://raw.githubusercontent.com/YaoXingjin/Typora-image/main/images/2024/01/20240115_143022_1234.jpg
```

这个链接可以直接在网页中访问，也可以在 Markdown 文档中正常显示。