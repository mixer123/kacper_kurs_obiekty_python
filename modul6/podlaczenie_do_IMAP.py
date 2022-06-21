import email
from email.header import decode_header
import imaplib
host = 's143.cyber-folks.pl'
port = 993
user = 'biuro@ecompus.pl'
password = 'JkisFQRz9VyWc2$'
imap_server = imaplib.IMAP4_SSL(host)
imap_server.login(user, password)
imap_server.select('INBOX')
# print('typ imap server select', (imap_server.select('INBOX')))
message_ids= imap_server.search(None, 'ALL')
# print('typ', type(message_ids[1]))
typ, data = message_ids

print('type data', type(data))
for m in data[0].split():
    typ, data = imap_server.fetch(m, '(RFC822)')
    message = email.message_from_bytes(data[0][1])
    subject, subject_encoding = decode_header(message['Subject'])[0]
    if subject_encoding is not None:
        subject = subject.decode('utf-8')
    email_from , from_encoding = decode_header(message['From'])[0]
    if from_encoding is not None:
        email_from = email_from.decode('utf-8')
    print(subject, email_from)
    quit()
    # Pobieranie załaczników
    for chunk in message.walk():
        print(chunk.get_filename())
        print(chunk.get_payload(decode=True))
        quit()