import csv
import re
import PyPDF4

def extract_text_by_chapter(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)
    chapters = {}
    current_chapter = None

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        if text:  # 确保页面有文本内容
            chapter_title_match = re.search(r'\b\d+: .+', text) 
            if chapter_title_match:
                current_chapter = chapter_title_match.group(0)
                chapters[current_chapter] = ""

            if current_chapter:
                chapters[current_chapter] += text

    pdf_file.close()
    return chapters

def save_chapters_to_csv(chapters, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Chapter', 'Content'])
        for chapter, content in chapters.items():
            writer.writerow([chapter, content])

# 调用函数
pdf_path = r'C:\Users\speed\Desktop\project1llama\Principles of Anatomy and Physiology.pdf' # 替换为 PDF 文件的实际路径
output_path = 'output_chapters.csv'
chapters = extract_text_by_chapter(pdf_path)
save_chapters_to_csv(chapters, output_path)
