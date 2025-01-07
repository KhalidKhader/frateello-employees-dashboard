import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQFAmlsEc4GFVVbHjz3HjEYntw7ITlJRm2AFkgcHXXUTj0M1I-bJQwpBRLWa2D60b7tmiy_Vop8wtMR/pub?output=csv'
df = pd.read_csv(sheet_url)


# Streamlit app setup
st.set_page_config(page_title="Employee Dashboard", layout="wide")
st.title("Employee Dashboard")


st.subheader("Employee Count by Job Title")
job_title_count = df['Job Title'].value_counts()
st.bar_chart(job_title_count)

st.subheader("Employment Status Distribution")
employment_status_count = df['Employment Status'].value_counts()
st.bar_chart(employment_status_count)

st.subheader("Years of Service Distribution")
years_of_service_count = df['Years Of Service'].value_counts()
st.bar_chart(years_of_service_count)

st.subheader("Nationality")
nationality = df['Nationality'].value_counts()
st.bar_chart(nationality)

st.subheader("Marital Status")
marital_status = df['Marital Status'].value_counts()
st.bar_chart(marital_status)

st.subheader("Education")
education = df['Education'].value_counts()
st.bar_chart(education)

# Add, Update, and Delete Employees Section
employee_names = df['Employee Name'].tolist()

# Display dropdown for selecting an employee
selected_employee = st.selectbox('Select an Employee', employee_names)

# Show employee details if selected
if selected_employee:
    selected_employee_data = df[df['Employee Name'] == selected_employee].iloc[0]
    st.write("### Employee Details")
    for col in selected_employee_data.index:
        st.write(f"**{col}:** {selected_employee_data[col]}")

    # Update employee details
    st.header("Update Employee")
    new_name = st.text_input('Update Name', value=selected_employee_data['Employee Name'])
    new_job_title = st.selectbox('Update Job Title', df['Job Title'].unique(), index=df['Job Title'].tolist().index(selected_employee_data['Job Title']))

    if st.button("Update"):
        df.loc[df['Employee Name'] == selected_employee, 'Employee Name'] = new_name
        df.loc[df['Employee Name'] == selected_employee, 'Job Title'] = new_job_title
        st.success(f"Employee {selected_employee} updated successfully!")
        # Update Google Sheets data
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    # Delete employee
    if st.button("Delete Employee"):
        df = df[df['Employee Name'] != selected_employee]
        st.success(f"Employee {selected_employee} deleted successfully!")
        # Update Google Sheets data
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

# Add new employee form
st.header("Add New Employee")
new_employee_name = st.text_input("Employee Name")
new_employee_id = st.text_input("Employee ID")
new_employee_hire_date = st.date_input("Hire Date")
new_employee_location = st.text_input("Location")
new_employee_sector = st.text_input("Sector")
new_employee_department = st.text_input("Department")
new_employee_job_title = st.text_input("Job Title")
new_employee_line_manager = st.text_input("Line Manager")
new_employee_birth_date = st.date_input("Birth Date")
new_employee_nationality = st.text_input("Nationality")
new_employee_email = st.text_input("Work Email")
new_employee_mobile = st.text_input("Mobile No.")
new_employee_phone = st.text_input("Phone No.")
new_employee_contract_start_date = st.date_input("Current Contract Start Date")
new_employee_status = st.text_input("Employment Status")
new_employee_work_days = st.text_input("Work Days")
new_employee_marital_status = st.text_input("Marital Status")
new_employee_education = st.text_input("Education")
new_employee_years_of_service = st.text_input("Years Of Service")

if st.button("Add Employee"):
    new_employee = {
        'Employee Name': new_employee_name,
        'ID': new_employee_id,
        'Hire Date': str(new_employee_hire_date),
        'Location': new_employee_location,
        'Sector': new_employee_sector,
        'Department': new_employee_department,
        'Job Title': new_employee_job_title,
        'Line Manager': new_employee_line_manager,
        'Birth Date': str(new_employee_birth_date),
        'Nationality': new_employee_nationality,
        'Work Email': new_employee_email,
        'Mobile No.': new_employee_mobile,
        'Phone No.': new_employee_phone,
        'Current Contract Start Date': str(new_employee_contract_start_date),
        'Employment Status': new_employee_status,
        'Work Days': new_employee_work_days,
        'Marital Status': new_employee_marital_status,
        'Education': new_employee_education,
        'Years Of Service': new_employee_years_of_service
    }
    df = df.append(new_employee, ignore_index=True)
    st.success("New employee added successfully!")
    # Update Google Sheets data
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

# Display the updated employee list
st.write("### Updated Employee List")
st.write(df)
