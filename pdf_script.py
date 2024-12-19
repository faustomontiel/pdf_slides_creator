import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_sections(pdf_path, output_dir, sections):
    """
    Split a PDF into sections based on the provided page ranges and save each section in a separate folder.

    :param pdf_path: Path to the input PDF file
    :param output_dir: Path to the directory where sections will be saved
    :param sections: Dictionary with section names as keys and page ranges as values
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the PDF
    reader = PdfReader(pdf_path)

    for section, (start_page, end_page) in sections.items():
        # Create a writer for the current section
        writer = PdfWriter()

        # Add pages to the writer
        for page_num in range(start_page - 1, end_page):  # Pages are 0-indexed in PyPDF2
            writer.add_page(reader.pages[page_num])

        # Save the section as a new PDF
        section_dir = os.path.join(output_dir, section)
        os.makedirs(section_dir, exist_ok=True)
        output_path = os.path.join(section_dir, f"{section}.pdf")
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"Section '{section}' saved to {output_path}")

if __name__ == "__main__":
    # Path to the input PDF
    pdf_path = "aws-slides.pdf"

    # Output directory
    output_dir = "output_sections"

    # Define the sections and their page ranges
    sections = {
        "IAM": (393, 447),
        "VPC": (448, 487),
        "EC2": (486, 636),
        "autoscaling": (637, 673),
        "EBS": (674, 699),
        "ELB": (700, 724),
        "S3": (725, 772),
        "RDS": (773, 837),
        "auroraDB": (838, 850),
        "DynamoDB": (851, 882),
        "ApplicationIntegration": (883, 912),
        "Amplify": (913, 918),
        "Serverless": (919, 941),
        "Route53": (942, 952),
        "CloudFront": (953, 982),
        "RestContent": (983, 1031),  # Adjust to the total number of pages if necessary
    }

    # Call the function
    split_pdf_by_sections(pdf_path, output_dir, sections)
