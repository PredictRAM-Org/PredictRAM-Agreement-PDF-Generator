import streamlit as st
from fpdf import FPDF
from io import BytesIO

def generate_agreement(name, email, contact_number, date, intern_location):
    pdf = FPDF()
    pdf.add_page()

    # Add company logo at the top of the page
    pdf.image("Predictra._logo.png", x=10, y=10, w=30)

    pdf.set_font("Arial", size=12)

    # Add content to the PDF
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True, align='L')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Dear {name},\n\n"
                               f"I am delighted & excited to welcome you to PredictRAM for Risk & Asset Management Training cum "
                               f"Training & Internship Program. At PredictRAM, we believe that our team is our biggest strength, "
                               f"and we take pride in hiring only the best and the brightest. We are confident that you would play a "
                               f"significant role in the overall success of the venture and wish you the most enjoyable, learning-packed, "
                               f"and truly meaningful training & internship experience with PredictRAM.\n\n"
                               f"Your appointment will be governed by the terms and conditions presented in Annexure A.\n\n"
                               f"We look forward to you joining us. Please do not hesitate to call us for any information you may need. "
                               f"Also, please sign the duplicate of this offer as your acceptance and forward the same to us.\n\n"
                               f"Congratulations!\n"
                               f"Team PredictRAM", align='L')

    # Add Annexure A
    pdf.ln(10)
    pdf.cell(200, 10, txt="Training & Training & Internship Agreement", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt="This Training & Training & Internship Agreement (this “Agreement”) is hereby entered into Day.", ln=True, align='L')
    pdf.cell(200, 10, txt="(“Effective Date”) - between the Intern and Company noted below, with respect to the Services and Project defined herein below.", ln=True, align='L')
    pdf.ln(10)
    pdf.cell(200, 10, txt="Intern Name:", ln=True, align='L')
    pdf.cell(200, 10, txt=f"{name}", ln=True, align='L')
    pdf.cell(200, 10, txt="Intern Email:", ln=True, align='L')
    pdf.cell(200, 10, txt=f"{email}", ln=True, align='L')
    pdf.cell(200, 10, txt="Contact Number:", ln=True, align='L')
    pdf.cell(200, 10, txt=f"{contact_number}", ln=True, align='L')
    pdf.cell(200, 10, txt="Intern Location:", ln=True, align='L')
    pdf.cell(200, 10, txt=f"{intern_location}", ln=True, align='L')  # <-- Added this line

    # ... (rest of the Annexure A content)

    return pdf.output(dest='S').encode('latin1')

def main():
    st.title("PredictRAM Agreement Generator")

    # User input
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    contact_number = st.text_input("Contact Number:")
    date = st.text_input("Date:")
    intern_location = st.text_input("Intern Location:")  # <-- Added this line

    if st.button("Generate Agreement"):
        if name and email and contact_number and date and intern_location:
            # Generate the PDF
            pdf_data = generate_agreement(name, email, contact_number, date, intern_location)

            # Download the PDF
            st.download_button(label="Download Agreement", data=pdf_data, file_name="PredictRAM_Agreement.pdf", key="download_button")

if __name__ == "__main__":
    main()
