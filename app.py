import streamlit as st
from fpdf import FPDF
from io import BytesIO

def generate_agreement(name, email, contact_number, date):
    pdf = FPDF()
    pdf.add_page()

    # Add company logo at the top of the page
    pdf.image("Predictram_logo.png", x=10, y=10, w=30)

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
    pdf.ln(10)
    pdf.cell(200, 10, txt="Company Representative Name:", ln=True, align='L')
    pdf.cell(200, 10, txt="(“SUBIR SINGH”):", ln=True, align='L')
    pdf.cell(200, 10, txt="Business Name: PredictRAM – Params Data Provider Pvt Ltd & Associate Companies.", ln=True, align='L')
    pdf.cell(200, 10, txt="Tel: 9873387612", ln=True, align='L')
    pdf.cell(200, 10, txt="Email: subir@predictram.com  i.subirsingh@gmail.com", ln=True, align='L')
    pdf.ln(10)
    pdf.cell(200, 10, txt="Terms & Conditions", ln=True, align='L')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="BACKGROUND: The Company has developed a comprehensive 6-month training and internship program focused on Risk and Asset Management (hereinafter referred to as the \"Program\"). The Program offers valuable training and practical experience to interns to prepare them for a career in the financial industry. It is important to note that the cost for joining this program is free. Upon successful completion of the Program, the Intern shall have the opportunity to work with the Company, associate company or partnered company in managing real client portfolios.", align='L')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="DURATION OF TRAINING & INTERNSHIP: The duration of training and internship program with the Company is for a period of six (6) months, commencing on the date that the Intern signs or accept this Agreement (the \"Start Date\") mentioned above.", align='L')
    pdf.ln(10)
    pdf.cell(200, 10, txt="PROGRAM DETAILS:", ln=True, align='L')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="1. NISM Research Analyst Exam Preparation: The Intern will receive recorded sessions and study materials to prepare for the NISM Research Analyst Exam.\n"
                               "2. Data-Driven Client Interaction: The Program will develop the Intern's skills in data-driven client engagement, utilizing analytics to assist clients in achieving their financial goals.\n"
                               "3. Alternative Data & Sentiment Analysis: The Intern will learn to analyze non-traditional data sources to assess a company's future performance by using economic data and other alternative parameters.\n"
                               "4. Company Management Conference Participation: The Program will familiarize the Intern with attending company management conferences, enabling them to ask insightful questions to top management.\n"
                               "5. Diverse Asset Class Management: The Intern will gain expertise in managing various asset classes, including traditional equities, modern digital assets and others.\n"
                               "6. Data Analytics Training: The Intern will receive training in data analytics using Python Basics.\n"
                               "7. Real Client Portfolio Management: Following successful clearance of NISM exams, the Intern will have the opportunity to manage real client portfolios, gaining hands-on experience.\n"
                               "8. ESG Analysis with Alternative Data: The Program will provide training on integrating ESG analysis into portfolio management using alternative data sources.\n"
                               "9. Regulatory Compliance: The Intern will receive training on the Code of Conduct for Financial Professionals, ethical standards, regulations, and practical scenarios.", align='L')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="COMPENSATION: Upon successful completion of the Program, the Company agrees to offer the Intern a starting monthly salary of INR 10,000 to manage real client portfolios. The terms and conditions of the Intern's employment with the Company, including but not limited to working hours, benefits, confidentiality, and termination procedures, shall be outlined in a separate employment agreement to be provided to the Intern upon successfully completion of the Program.", align='L')

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
