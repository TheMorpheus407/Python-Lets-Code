from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

def get_meta(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        nop = pdf.getNumPages()
    print(info)
    print(nop)

def extract_text(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page_one = pdf.getPage(1)
        print(page_one)
        print(type(page_one))
        text = page_one.extractText()
        print(text)

def split_pdf(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for page in range(pdf.getNumPages()):
            writer = PdfFileWriter()
            writer.addPage(pdf.getPage(page))
            with open(f"{page}.pdf", "wb") as f_out:
                writer.write(f_out)

def merge_pdf(input_paths, output_path):
    writer = PdfFileWriter()
    for i in input_paths:
        pdf_reader = PdfFileReader(i)
        for page in range(pdf_reader.getNumPages()):
            writer.addPage(pdf_reader.getPage(page))
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

def lazy_merge(input_paths, output_path):
    pdf_merger = PdfFileMerger()
    for i in input_paths:
        pdf_merger.append(i)
    with open(output_path, "wb") as f_out:
        pdf_merger.write(f_out)

if __name__ == '__main__':
    path = r"G:\Tuts\Uploaded\Algorithmen und Datenstrukturen\Bonus\Radix_LSD_Sort.pdf"
    lazy_merge(["2.pdf", "1.pdf"], "out.pdf")