"""
图片转换脚本：将原始图片转换为 96x128 WebP 格式（3:4 比例，中心裁切）
"""
from PIL import Image
import os

# 源目录和目标目录
SRC_DIR = "ComfyUI_ZIP_00001_tqnpe_1767959385"
DST_DIR = "images"

# 目标尺寸：3:4 比例，长边 128px → 96x128
TARGET_WIDTH = 96
TARGET_HEIGHT = 128

# 文件名映射（索引 -> 新文件名）
FILE_NAMES = [
    # Close-up (0-31)
    "closeup_front_low",
    "closeup_front-right_low",
    "closeup_right_low",
    "closeup_back-right_low",
    "closeup_back_low",
    "closeup_back-left_low",
    "closeup_left_low",
    "closeup_front-left_low",
    "closeup_front_eye",
    "closeup_front-right_eye",
    "closeup_right_eye",
    "closeup_back-right_eye",
    "closeup_back_eye",
    "closeup_back-left_eye",
    "closeup_left_eye",
    "closeup_front-left_eye",
    "closeup_front_elevated",
    "closeup_front-right_elevated",
    "closeup_right_elevated",
    "closeup_back-right_elevated",
    "closeup_back_elevated",
    "closeup_back-left_elevated",
    "closeup_left_elevated",
    "closeup_front-left_elevated",
    "closeup_front_high",
    "closeup_front-right_high",
    "closeup_right_high",
    "closeup_back-right_high",
    "closeup_back_high",
    "closeup_back-left_high",
    "closeup_left_high",
    "closeup_front-left_high",
    # Medium Shot (32-63)
    "medium_front_low",
    "medium_front-right_low",
    "medium_right_low",
    "medium_back-right_low",
    "medium_back_low",
    "medium_back-left_low",
    "medium_left_low",
    "medium_front-left_low",
    "medium_front_eye",
    "medium_front-right_eye",
    "medium_right_eye",
    "medium_back-right_eye",
    "medium_back_eye",
    "medium_back-left_eye",
    "medium_left_eye",
    "medium_front-left_eye",
    "medium_front_elevated",
    "medium_front-right_elevated",
    "medium_right_elevated",
    "medium_back-right_elevated",
    "medium_back_elevated",
    "medium_back-left_elevated",
    "medium_left_elevated",
    "medium_front-left_elevated",
    "medium_front_high",
    "medium_front-right_high",
    "medium_right_high",
    "medium_back-right_high",
    "medium_back_high",
    "medium_back-left_high",
    "medium_left_high",
    "medium_front-left_high",
    # Wide Shot (64-95)
    "wide_front_low",
    "wide_front-right_low",
    "wide_right_low",
    "wide_back-right_low",
    "wide_back_low",
    "wide_back-left_low",
    "wide_left_low",
    "wide_front-left_low",
    "wide_front_eye",
    "wide_front-right_eye",
    "wide_right_eye",
    "wide_back-right_eye",
    "wide_back_eye",
    "wide_back-left_eye",
    "wide_left_eye",
    "wide_front-left_eye",
    "wide_front_elevated",
    "wide_front-right_elevated",
    "wide_right_elevated",
    "wide_back-right_elevated",
    "wide_back_elevated",
    "wide_back-left_elevated",
    "wide_left_elevated",
    "wide_front-left_elevated",
    "wide_front_high",
    "wide_front-right_high",
    "wide_right_high",
    "wide_back-right_high",
    "wide_back_high",
    "wide_back-left_high",
    "wide_left_high",
    "wide_front-left_high",
]


def center_crop_resize(img, target_w, target_h):
    """中心裁切并缩放到目标尺寸"""
    w, h = img.size
    target_ratio = target_w / target_h
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        # 图片太宽，裁切左右
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        # 图片太高，裁切上下
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    
    return img.resize((target_w, target_h), Image.LANCZOS)


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    
    for i, name in enumerate(FILE_NAMES):
        src_file = os.path.join(SRC_DIR, f"ComfyUI_ZIP_{i:05d}.png")
        dst_file = os.path.join(DST_DIR, f"{name}.webp")
        
        if not os.path.exists(src_file):
            print(f"[SKIP] {src_file} not found")
            continue
        
        img = Image.open(src_file)
        img = center_crop_resize(img, TARGET_WIDTH, TARGET_HEIGHT)
        img.save(dst_file, "WEBP", quality=85)
        print(f"[OK] {src_file} -> {dst_file}")
    
    print(f"\nDone! Converted {len(FILE_NAMES)} images to {DST_DIR}/")


if __name__ == "__main__":
    main()
