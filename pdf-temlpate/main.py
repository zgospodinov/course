import os
from fpdf import FPDF
import pandas as pd

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define output directory
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output')

df = pd.read_csv(os.path.join(SCRIPT_DIR, 'topics.csv'))

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()  

    # Add gray background for header
    pdf.set_fill_color(240, 240, 240)  # Light gray
    pdf.rect(0, 0, 220, 25, 'F')  # x, y, width, height, style='F' for fill

    # Add topic text
    pdf.set_font("Arial", size=22, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='L')
    
    # Add horizontal lines
    # Starting y position (just after the topic)
    y_position = 40
    
    # Draw lines until near the bottom of the page (297mm is A4 height)
    while y_position < 287:  # Leave some space at bottom for the footer
        pdf.line(10, y_position, 200, y_position)  # 10mm from left, 200mm is near right edge
        y_position += 10  # Space between lines
    
    # Footer - Set position to bottom of page
    pdf.set_y(287)  # Position footer near bottom
    pdf.set_font("Arial", size=8, style='I')
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align='R')


    
# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Save PDF in the output directory
pdf.output(os.path.join(OUTPUT_DIR, 'output.pdf'))
