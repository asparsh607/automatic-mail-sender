import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

# Setting the email server
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Loading environment variables
curr_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = curr_dir / ".env"
load_dotenv(envars)

# Reading from environment
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")

def send_mail(subject: str, receiver_email: str, cc_emails=None, bcc_emails=None):
    """
    Create an EmailMessage object to send an email.

    Args:
        subject (str): The subject of the email.
        receiver_email (str): The recipient's email address.
        cc_emails (list[str], optional): List of email addresses to CC. Default is None.
        bcc_emails (list[str], optional): List of email addresses to BCC. Default is None.

    Returns:
        EmailMessage: An EmailMessage object ready to be sent.
    """
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    if cc_emails:
        msg["CC"] = ", ".join(cc_emails)

    if bcc_emails:
        msg["BCC"] = ", ".join(bcc_emails)

    msg.set_content(
        f"""
        {subject}
        Hi {receiver_email}.

        EMAIL BODY
        """
    )
    return msg

# Your email configuration
my_email = sender_email
password = sender_password
rec_email = ["test1@gmail.com", "test2@gmail.com"]  # List of receiver's email addresses.
cc_email = ["cc1@gmail.com", "cc2@gmail.com"]  # List of CC email addresses.
bcc_email = ["bcc1@gmail.com", "bcc2@gmail.com"]  # List of BCC email addresses.

EMAIL_SERVER = "smtp.gmail.com"
PORT = 587

# Create and send the email
if __name__ == "__main__":
    for email in rec_email:
        with smtplib.SMTP(host=EMAIL_SERVER, port=PORT) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=send_mail("Test Email", email, cc_emails=cc_email, bcc_emails=bcc_email).as_string().encode("utf-8")
            )
        print(f"Email Sent to {email}!")

    print(f"{len(rec_email)} Emails Sent Successfully!")
