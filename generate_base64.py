"""
生成 Base64 图片数据的 JS 文件
"""
import base64
import os

IMAGE_DIR = "images"
OUTPUT_FILE = "js/angle_prompt_images.js"

FILE_NAMES = [
    # Close-up (0-31)
    "closeup_front_low", "closeup_front-right_low", "closeup_right_low", "closeup_back-right_low",
    "closeup_back_low", "closeup_back-left_low", "closeup_left_low", "closeup_front-left_low",
    "closeup_front_eye", "closeup_front-right_eye", "closeup_right_eye", "closeup_back-right_eye",
    "closeup_back_eye", "closeup_back-left_eye", "closeup_left_eye", "closeup_front-left_eye",
    "closeup_front_elevated", "closeup_front-right_elevated", "closeup_right_elevated", "closeup_back-right_elevated",
    "closeup_back_elevated", "closeup_back-left_elevated", "closeup_left_elevated", "closeup_front-left_elevated",
    "closeup_front_high", "closeup_front-right_high", "closeup_right_high", "closeup_back-right_high",
    "closeup_back_high", "closeup_back-left_high", "closeup_left_high", "closeup_front-left_high",
    # Medium Shot (32-63)
    "medium_front_low", "medium_front-right_low", "medium_right_low", "medium_back-right_low",
    "medium_back_low", "medium_back-left_low", "medium_left_low", "medium_front-left_low",
    "medium_front_eye", "medium_front-right_eye", "medium_right_eye", "medium_back-right_eye",
    "medium_back_eye", "medium_back-left_eye", "medium_left_eye", "medium_front-left_eye",
    "medium_front_elevated", "medium_front-right_elevated", "medium_right_elevated", "medium_back-right_elevated",
    "medium_back_elevated", "medium_back-left_elevated", "medium_left_elevated", "medium_front-left_elevated",
    "medium_front_high", "medium_front-right_high", "medium_right_high", "medium_back-right_high",
    "medium_back_high", "medium_back-left_high", "medium_left_high", "medium_front-left_high",
    # Wide Shot (64-95)
    "wide_front_low", "wide_front-right_low", "wide_right_low", "wide_back-right_low",
    "wide_back_low", "wide_back-left_low", "wide_left_low", "wide_front-left_low",
    "wide_front_eye", "wide_front-right_eye", "wide_right_eye", "wide_back-right_eye",
    "wide_back_eye", "wide_back-left_eye", "wide_left_eye", "wide_front-left_eye",
    "wide_front_elevated", "wide_front-right_elevated", "wide_right_elevated", "wide_back-right_elevated",
    "wide_back_elevated", "wide_back-left_elevated", "wide_left_elevated", "wide_front-left_elevated",
    "wide_front_high", "wide_front-right_high", "wide_right_high", "wide_back-right_high",
    "wide_back_high", "wide_back-left_high", "wide_left_high", "wide_front-left_high",
]

def main():
    base64_list = []
    
    for name in FILE_NAMES:
        filepath = os.path.join(IMAGE_DIR, f"{name}.webp")
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
                base64_list.append(f"data:image/webp;base64,{data}")
                print(f"[OK] {filepath}")
        else:
            base64_list.append("")
            print(f"[SKIP] {filepath} not found")
    
    # Write JS file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("// Auto-generated Base64 image data\n")
        f.write("export const IMAGE_DATA = [\n")
        for i, data in enumerate(base64_list):
            f.write(f'    "{data}",\n')
        f.write("];\n")
    
    print(f"\nDone! Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
