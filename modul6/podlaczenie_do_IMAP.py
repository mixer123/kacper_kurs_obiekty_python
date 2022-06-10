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
message_ids= imap_server.search(None, 'ALL')
typ, data = message_ids
for m in data[0].split():
    typ, data = imap_server.fetch(m, '(RFC822)')
    print(m, data[0][1])
    quit()