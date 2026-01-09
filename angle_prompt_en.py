class AnglePromptEN:
    """ComfyUI custom node for camera angle prompts (English) with dynamic prompt selection"""
    
    SHOT_TYPES = ["Close-up", "Medium Shot", "Wide Shot"]
    
    PROMPTS = {
        "Close-up": [
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
        ],
        "Medium Shot": [
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
        ],
        "Wide Shot": [
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
        ],
    }

    CONCAT_MODES = ["prefix", "suffix"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "shot_type": (cls.SHOT_TYPES, {"default": "Close-up"}),
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
        # Allow any prompt_select value since it's dynamically generated
        return True

    @classmethod
    def IS_CHANGED(cls, shot_type, prompt_select=None, **kwargs):
        return float("nan")

    def generate_prompt(self, shot_type, concat_mode="prefix", input_prompt=None, unique_id=None, prompt_select=None):
        # Get prompt from the dynamic widget value
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
    "AnglePromptEN": AnglePromptEN
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnglePromptEN": "角度提示词_EN"
}
