"""可视化角度提示词节点"""

class QwenAnglePromptVisual:
    """ComfyUI visual node for camera angle prompts with image grid selection"""
    
    PROMPTS_EN = [
        # Close-up (0-31)
        "front view low-angle shot close-up",
        "front-right quarter view low-angle shot close-up",
        "right side view low-angle shot close-up",
        "back-right quarter view low-angle shot close-up",
        "back view low-angle shot close-up",
        "back-left quarter view low-angle shot close-up",
        "left side view low-angle shot close-up",
        "front-left quarter view low-angle shot close-up",
        "front view eye-level shot close-up",
        "front-right quarter view eye-level shot close-up",
        "right side view eye-level shot close-up",
        "back-right quarter view eye-level shot close-up",
        "back view eye-level shot close-up",
        "back-left quarter view eye-level shot close-up",
        "left side view eye-level shot close-up",
        "front-left quarter view eye-level shot close-up",
        "front view elevated shot close-up",
        "front-right quarter view elevated shot close-up",
        "right side view elevated shot close-up",
        "back-right quarter view elevated shot close-up",
        "back view elevated shot close-up",
        "back-left quarter view elevated shot close-up",
        "left side view elevated shot close-up",
        "front-left quarter view elevated shot close-up",
        "front view high-angle shot close-up",
        "front-right quarter view high-angle shot close-up",
        "right side view high-angle shot close-up",
        "back-right quarter view high-angle shot close-up",
        "back view high-angle shot close-up",
        "back-left quarter view high-angle shot close-up",
        "left side view high-angle shot close-up",
        "front-left quarter view high-angle shot close-up",
        # Medium Shot (32-63)
        "front view low-angle shot medium shot",
        "front-right quarter view low-angle shot medium shot",
        "right side view low-angle shot medium shot",
        "back-right quarter view low-angle shot medium shot",
        "back view low-angle shot medium shot",
        "back-left quarter view low-angle shot medium shot",
        "left side view low-angle shot medium shot",
        "front-left quarter view low-angle shot medium shot",
        "front view eye-level shot medium shot",
        "front-right quarter view eye-level shot medium shot",
        "right side view eye-level shot medium shot",
        "back-right quarter view eye-level shot medium shot",
        "back view eye-level shot medium shot",
        "back-left quarter view eye-level shot medium shot",
        "left side view eye-level shot medium shot",
        "front-left quarter view eye-level shot medium shot",
        "front view elevated shot medium shot",
        "front-right quarter view elevated shot medium shot",
        "right side view elevated shot medium shot",
        "back-right quarter view elevated shot medium shot",
        "back view elevated shot medium shot",
        "back-left quarter view elevated shot medium shot",
        "left side view elevated shot medium shot",
        "front-left quarter view elevated shot medium shot",
        "front view high-angle shot medium shot",
        "front-right quarter view high-angle shot medium shot",
        "right side view high-angle shot medium shot",
        "back-right quarter view high-angle shot medium shot",
        "back view high-angle shot medium shot",
        "back-left quarter view high-angle shot medium shot",
        "left side view high-angle shot medium shot",
        "front-left quarter view high-angle shot medium shot",
        # Wide Shot (64-95)
        "front view low-angle shot wide shot",
        "front-right quarter view low-angle shot wide shot",
        "right side view low-angle shot wide shot",
        "back-right quarter view low-angle shot wide shot",
        "back view low-angle shot wide shot",
        "back-left quarter view low-angle shot wide shot",
        "left side view low-angle shot wide shot",
        "front-left quarter view low-angle shot wide shot",
        "front view eye-level shot wide shot",
        "front-right quarter view eye-level shot wide shot",
        "right side view eye-level shot wide shot",
        "back-right quarter view eye-level shot wide shot",
        "back view eye-level shot wide shot",
        "back-left quarter view eye-level shot wide shot",
        "left side view eye-level shot wide shot",
        "front-left quarter view eye-level shot wide shot",
        "front view elevated shot wide shot",
        "front-right quarter view elevated shot wide shot",
        "right side view elevated shot wide shot",
        "back-right quarter view elevated shot wide shot",
        "back view elevated shot wide shot",
        "back-left quarter view elevated shot wide shot",
        "left side view elevated shot wide shot",
        "front-left quarter view elevated shot wide shot",
        "front view high-angle shot wide shot",
        "front-right quarter view high-angle shot wide shot",
        "right side view high-angle shot wide shot",
        "back-right quarter view high-angle shot wide shot",
        "back view high-angle shot wide shot",
        "back-left quarter view high-angle shot wide shot",
        "left side view high-angle shot wide shot",
        "front-left quarter view high-angle shot wide shot",
    ]
    
    PROMPTS_CN = [
        # 特写镜头组 (0-31)
        "正面低仰角特写",
        "右前方低仰角特写",
        "右侧面低仰角特写",
        "右后方低仰角特写",
        "背面低仰角特写",
        "左后方低仰角特写",
        "左侧面低仰角特写",
        "左前方低仰角特写",
        "正面平视特写",
        "右前方平视特写",
        "右侧面平视特写",
        "右后方平视特写",
        "背面平视特写",
        "左后方平视特写",
        "左侧面平视特写",
        "左前方平视特写",
        "正面高位特写",
        "右前方高位特写",
        "右侧面高位特写",
        "右后方高位特写",
        "背面高位特写",
        "左后方高位特写",
        "左侧面高位特写",
        "左前方高位特写",
        "正面高角度俯拍特写",
        "右前方高角度俯拍特写",
        "右侧面高角度俯拍特写",
        "右后方高角度俯拍特写",
        "背面高角度俯拍特写",
        "左后方高角度俯拍特写",
        "左侧面高角度俯拍特写",
        "左前方高角度俯拍特写",
        # 中景镜头组 (32-63)
        "正面低仰角中景",
        "右前方低仰角中景",
        "右侧面低仰角中景",
        "右后方低仰角中景",
        "背面低仰角中景",
        "左后方低仰角中景",
        "左侧面低仰角中景",
        "左前方低仰角中景",
        "正面平视中景",
        "右前方平视中景",
        "右侧面平视中景",
        "右后方平视中景",
        "背面平视中景",
        "左后方平视中景",
        "左侧面平视中景",
        "左前方平视中景",
        "正面高位中景",
        "右前方高位中景",
        "右侧面高位中景",
        "右后方高位中景",
        "背面高位中景",
        "左后方高位中景",
        "左侧面高位中景",
        "左前方高位中景",
        "正面高角度俯拍中景",
        "右前方高角度俯拍中景",
        "右侧面高角度俯拍中景",
        "右后方高角度俯拍中景",
        "背面高角度俯拍中景",
        "左后方高角度俯拍中景",
        "左侧面高角度俯拍中景",
        "左前方高角度俯拍中景",
        # 全景镜头组 (64-95)
        "正面低仰角全景",
        "右前方低仰角全景",
        "右侧面低仰角全景",
        "右后方低仰角全景",
        "背面低仰角全景",
        "左后方低仰角全景",
        "左侧面低仰角全景",
        "左前方低仰角全景",
        "正面平视全景",
        "右前方平视全景",
        "右侧面平视全景",
        "右后方平视全景",
        "背面平视全景",
        "左后方平视全景",
        "左侧面平视全景",
        "左前方平视全景",
        "正面高位全景",
        "右前方高位全景",
        "右侧面高位全景",
        "右后方高位全景",
        "背面高位全景",
        "左后方高位全景",
        "左侧面高位全景",
        "左前方高位全景",
        "正面高角度俯拍全景",
        "右前方高角度俯拍全景",
        "右侧面高角度俯拍全景",
        "右后方高角度俯拍全景",
        "背面高角度俯拍全景",
        "左后方高角度俯拍全景",
        "左侧面高角度俯拍全景",
        "左前方高角度俯拍全景",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "language": ("BOOLEAN", {"default": True, "label_on": "EN", "label_off": "CN"}),
                "output_mode": (["multi_line", "string_list"], {"default": "multi_line"}),
                "selected_indices": ("STRING", {"default": ""}),
            },
            "optional": {
                "input_prompt": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompt_text", "prompt_list")
    FUNCTION = "generate_prompt"
    CATEGORY = "QwenEditAnglePrompt"

    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs):
        return True

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("nan")

    def generate_prompt(self, language, output_mode, selected_indices, input_prompt=None):
        if not selected_indices or selected_indices.strip() == "":
            return ("", "")
        
        prompts = self.PROMPTS_EN if language else self.PROMPTS_CN
        
        indices = [int(i.strip()) for i in selected_indices.split(",") if i.strip().isdigit()]
        indices = [i for i in indices if 0 <= i < 96]
        
        selected_prompts = [f"<sks> {prompts[i]}" for i in indices]
        
        if output_mode == "multi_line":
            prompt_text = "\n".join(selected_prompts)
        else:
            prompt_text = ", ".join(selected_prompts)
        
        prompt_list = str(selected_prompts)
        
        if input_prompt:
            prompt_text = f"{input_prompt}\n{prompt_text}"
        
        return (prompt_text, prompt_list)


NODE_CLASS_MAPPINGS = {
    "QwenAnglePromptVisual": QwenAnglePromptVisual
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QwenAnglePromptVisual": "千问角度提示词_可视化"
}
