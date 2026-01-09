class AnglePromptCN:
    """ComfyUI custom node for camera angle prompts (Chinese) with dynamic prompt selection"""
    
    SHOT_TYPES = ["特写镜头组", "中景镜头组", "全景镜头组"]
    CONCAT_MODES = ["prefix", "suffix"]
    
    PROMPTS = {
        "特写镜头组": [
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
        ],
        "中景镜头组": [
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
        ],
        "全景镜头组": [
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
        ],
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "shot_type": (cls.SHOT_TYPES, {"default": "特写镜头组"}),
                "concat_mode": (cls.CONCAT_MODES, {"default": "prefix"}),
            },
            "optional": {
                "input_prompt": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "prompt"

    @classmethod
    def VALIDATE_INPUTS(cls, shot_type, prompt_select=None, **kwargs):
        return True

    @classmethod
    def IS_CHANGED(cls, shot_type, prompt_select=None, **kwargs):
        return float("nan")

    def generate_prompt(self, shot_type, concat_mode="prefix", input_prompt=None, unique_id=None, prompt_select=None):
        if prompt_select is None:
            prompt_select = self.PROMPTS[shot_type][0]
        
        angle_prompt = f"<sks> {prompt_select}"
        
        if input_prompt:
            if concat_mode == "prefix":
                output = f"{angle_prompt}, {input_prompt}"
            else:
                output = f"{input_prompt}, {angle_prompt}"
        else:
            output = angle_prompt
        
        return (output,)


NODE_CLASS_MAPPINGS = {
    "AnglePromptCN": AnglePromptCN
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnglePromptCN": "角度提示词_CN"
}
