import os
import re
from PIL import Image

def images_to_pdf(img_dir, output_pdf):
    """
    将指定目录中的图片按编号顺序导出为 PDF 文件。
    
    参数:
        img_dir (str): 图片存放的目录路径。
        output_pdf (str): 导出的 PDF 文件路径。
    """
    # 获取图片列表，并按编号排序
    img_files = [f for f in os.listdir(img_dir) if f.endswith(".png")]
    img_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    print(img_files) 
    
    if not img_files:
        raise ValueError("No images found in the specified directory.")
    
    # 打开图片，确保所有图片都以 RGB 模式加载
    images = [Image.open(os.path.join(img_dir, img)).convert("RGB") for img in img_files]
    
    # 将第一张图片作为基础 PDF，并添加其他图片
    base_image = images[0]
    base_image.save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF successfully saved to {output_pdf}")

if __name__ == '__main__':
    image_path = 'res'
    pdf_path = 'res.pdf'
    images_to_pdf(image_path, pdf_path)
