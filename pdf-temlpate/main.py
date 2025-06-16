import os
from fpdf import FPDF
import pandas as pd

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define output directory
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output')

df = pd.read_csv(os.path.join(SCRIPT_DIR, 'topics.csv'))

pdf = FPDF(orientation='P', unit='mm', format='A4')
for index, row in df.iterrows():
    pdf.add_page()  
    pdf.set_font("Arial", size=22, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='L')
    pdf.line(10, 23, 200, 23)

    
# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Save PDF in the output directory
pdf.output(os.path.join(OUTPUT_DIR, 'output.pdf'))
