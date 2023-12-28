import streamlit as st
from fpdf import FPDF
from io import BytesIO

def generate_agreement(name, email, contact_number, date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add company logo at the center of the page
    logo_width = 30
    page_width = pdf.w
    x_position = (page_width - logo_width) / 2

    pdf.image("Predictram_logo.png", x=x_position, y=10, w=logo_width)

    # Add content to the PDF
    # Adjust Y-coordinate to align date with the logo
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True, align='L') 

    pdf.multi_cell(0, 10, txt=f"Dear {name},\n\n"
                               f"I am delighted & excited to welcome you to PredictRAM for Risk & Asset Management Training cum "
                               f"Training & Internship Program. At PredictRAM, we believe that our team is our biggest strength, "
                               f"and we take pride in hiring only the best and the brightest. We are confident that you would play a "
                               f"significant role in the overall success of the venture and wish you the most enjoyable, learning-packed, "
                               f"and truly meaningful training & internship experience with PredictRAM.\n\n"
                               f"Your appointment will be governed by the terms and conditions presented in Annexure A.\n\n"
                               f"We look forward to you joining us. Please do not hesitate to call us for any information you may need. "
                               f"Also, please sign the duplicate of this offer as your acceptance and forward the same to us.\n\n"
                   f"I am delighted & excited to welcome you to PredictRAM for Risk & Asset Management Training cum "
                               f"Training & Internship Program. At PredictRAM, we believe that our team is our biggest strength, "
                               f"and we take pride in hiring only the best and the brightest. We are confident that you would play a "
                               f"significant role in the overall success of the venture and wish you the most enjoyable, learning-packed, "
                               f"and truly meaningful training & internship experience with PredictRAM.\n\n"
                               f"Your appointment will be governed by the terms and conditions presented in Annexure A.\n\n"
                               f"We look forward to you joining us. Please do not hesitate to call us for any information you may need. "
                               f"Also, please sign the duplicate of this offer as your acceptance and forward the same to us.\n\n"f"I am delighted & excited to welcome you to PredictRAM for Risk & Asset Management Training cum "
                               f"Training & Internship Program. At PredictRAM, we believe that our team is our biggest strength, "
                               f"and we take pride in hiring only the best and the brightest. We are confident that you would play a "
                               f"significant role in the overall success of the venture and wish you the most enjoyable, learning-packed, "
                               f"and truly meaningful training & internship experience with PredictRAM.\n\n"
                               f"Your appointment will be governed by the terms and conditions presented in Annexure A.\n\n"
                               f"We look forward to you joining us. Please do not hesitate to call us for any information you may need. "
                               f"Also, please sign the duplicate of this offer as your acceptance and forward the same to us.\n\n"f"I am delighted & excited to welcome you to PredictRAM for Risk & Asset Management Training cum "
                               f"Training & Internship Program. At PredictRAM, we believe that our team is our biggest strength, "
                               f"and we take pride in hiring only the best and the brightest. We are confident that you would play a "
                               f"significant role in the overall success of the venture and wish you the most enjoyable, learning-packed, "
                               f"and truly meaningful training & internship experience with PredictRAM.\n\n"
                               f"Your appointment will be governed by the terms and conditions presented in Annexure A.\n\n"
                               f"We look forward to you joining us. Please do not hesitate to call us for any information you may need. "
                               f"Also, please sign the duplicate of this offer as your acceptance and forward the same to us.\n\n"f"I am delighted & excited to welcome you to PredictRAM for Risk & Asset Management Training cum "
                               f"Training & Internship Program. At PredictRAM, we believe that our team is our biggest strength, "
                               f"and we take pride in hiring only the best and the brightest. We are confident that you would play a "
                               f"significant role in the overall success of the venture and wish you the most enjoyable, learning-packed, "
                               f"and truly meaningful training & internship experience with PredictRAM.\n\n"
                               f"Your appointment will be governed by the terms and conditions presented in Annexure A.\n\n"
                               f"We look forward to you joining us. Please do not hesitate to call us for any information you may need. "
                               f"Also, please sign the duplicate of this offer as your acceptance and forward the same to us.\n\n"
                               f"Congratulations!\n"
                               f"Team PredictRAM", align='L')

    return pdf.output(dest='S').encode('latin1')

def main():
    st.title("PredictRAM Agreement Generator")

    # User input
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    contact_number = st.text_input("Contact Number:")
    date = st.text_input("Date:")

    if st.button("Generate Agreement"):
        if name and email and contact_number and date:
            # Generate the PDF
            pdf_data = generate_agreement(name, email, contact_number, date)

            # Download the PDF
            st.download_button(label="Download Agreement", data=pdf_data, file_name="PredictRAM_Agreement.pdf", key="download_button")

if __name__ == "__main__":
    main()
