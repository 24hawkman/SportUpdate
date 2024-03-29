import smtplib

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
    # Collect personal data from local file
    info_file = open('info.txt', 'r')
    info = info_file.readlines()
    info_file.close()
    phone = info[0]
    email = info[1]
    pw = info[2]

    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = phone + '{}'.format(carriers['verizon'])
    auth = (email, pw)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail( auth[0], to_number, message)