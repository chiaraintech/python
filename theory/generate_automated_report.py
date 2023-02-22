import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to collect sales data from a database or CSV file
def collect_sales_data():
    sales_data = pd.read_csv('sales_data.csv')
    return sales_data

# Function to collect inventory data from a database or CSV file
def collect_inventory_data():
    inventory_data = pd.read_csv('inventory_data.csv')
    return inventory_data

# Function to generate weekly sales report
def generate_sales_report(sales_data, inventory_data):
    weekly_sales = sales_data.groupby('product')['sales'].sum().reset_index()
    top_selling_products = weekly_sales.nlargest(3, 'sales')
    inventory_levels = inventory_data.groupby('product')['quantity'].sum().reset_index()
    report_data = pd.merge(top_selling_products, inventory_levels, on='product')
    return report_data

# Function to generate the email message
def generate_email_message(report_data):
    message = MIMEMultipart()
    message['Subject'] = 'Weekly Sales Report'
    message['From'] = 'sales@example.com'
    message['To'] = 'manager@example.com'
    text = MIMEText(report_data.to_html(), 'html')
    message.attach(text)
    return message

# Function to send the email
def send_email(message):
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'sales@example.com'
    smtp_password = 'password'
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_username, smtp_password)
    smtp_connection.send_message(message)
    smtp_connection.quit()

# Schedule the report to be generated and emailed every Monday
if datetime.datetime.today().weekday() == 0:  # Check if today is Monday
    sales_data = collect_sales_data()
    inventory_data = collect_inventory_data()
    report_data = generate_sales_report(sales_data, inventory_data)
    message = generate_email_message(report_data)
    send_email(message)
