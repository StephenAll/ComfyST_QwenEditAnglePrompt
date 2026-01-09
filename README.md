# ComfyST_QwenEditAnglePrompt

ComfyUI 自定义节点插件，用于生成相机角度提示词。

## 节点

- **千问角度提示词_CN** - 中文角度提示词
- **QwenAnglePrompt_EN** - 英文角度提示词

## 功能

- 支持三种镜头类型：特写/中景/全景 (Close-up/Medium Shot/Wide Shot)
- 动态提示词选择，根据镜头类型自动切换可选提示词
- 支持前缀/后缀拼接模式
- 可选提示词输入端口，方便串联使用

## 安装

将本仓库克隆到 `ComfyUI/custom_nodes/` 目录：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/StephenAll/ComfyST_QwenEditAnglePrompt.git
```

重启 ComfyUI 即可使用。

## 参数说明

| 参数 | 说明 |
|------|------|
| camera | 镜头类型选择 |
| prompt | 角度提示词选择（动态） |
| splicing | 拼接模式：prefix（前缀）/ suffix（后缀） |
| input_prompt | 可选输入，用于拼接其他提示词 |
