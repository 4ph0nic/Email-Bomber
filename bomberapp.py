import smtplib
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

# Set up the main window
window = QtWidgets.QWidget()
layout = QtWidgets.QFormLayout()
window.setLayout(layout)

# Add a line edit for the recipients
recipients_edit = QtWidgets.QLineEdit()
layout.addRow("Recipients:", recipients_edit)

# Add a line edit for the subject
subject_edit = QtWidgets.QLineEdit()
layout.addRow("Subject:", subject_edit)

# Add a text edit for the body
body_edit = QtWidgets.QTextEdit()
layout.addRow("Body:", body_edit)

# Add a combo box for the SMTP server
server_combo = QtWidgets.QComboBox()
server_combo.addItems(["Gmail", "Outlook"])
layout.addRow("Server:", server_combo)

# Add a line edit for the email address
email_edit = QtWidgets.QLineEdit()
layout.addRow("Email:", email_edit)

# Add a line edit for the password
password_edit = QtWidgets.QLineEdit()
password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
layout.addRow("Password:", password_edit)

# Add a spin box for selecting the number of emails to send
num_emails_spin_box = QtWidgets.QSpinBox()
num_emails_spin_box.setMinimum(1)
layout.addRow("Number of emails:", num_emails_spin_box)

# Add a button for sending the emails
send_button = QtWidgets.QPushButton("Send")
layout.addRow(send_button)

# Add a label for displaying the status of the email send operation
status_label = QtWidgets.QLabel()
layout.addRow("Status:", status_label)

# Set up the "Send" button click event
def send_emails():
    # Get the recipients and subject/body from the UI
    recipients_string = recipients_edit.text()
    recipients = recipients_string.split(',')
    subject = subject_edit.text()
    body = body_edit.toPlainText()

    # Get the SMTP server choice and email/password
    server_choice = server_combo.currentText()
    if server_choice == 'Gmail':
        server = smtplib.SMTP('smtp.gmail.com', 587)
    elif server_choice == 'Outlook':
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    else:
        status_label.setText("Invalid server choice. Exiting.")
        return

    email = email_edit.text()
    password = password_edit.text()
    server.starttls()
    server.login(email, password)

    # Get the number of emails to send from the spin box
    num_emails = num_emails_spin_box.value()

    # Make sure num_emails is not greater than the length of the recipients list
    if num_emails > len(recipients):
        num_emails = len(recipients)

    # Send the emails
    for i in range(num_emails):
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail('', recipients[i], message)

    server.quit()
    status_label.setText("Emails sent successfully.")

send_button.clicked.connect(send_emails)


send_button.clicked.connect(send_emails)

# Show the window
window.show()
app.exec_()

