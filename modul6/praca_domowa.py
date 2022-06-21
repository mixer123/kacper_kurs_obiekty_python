'''
Opis zadania
Przygotuj klienta pocztowego, który będzie w stanie zalogować się
na wskazaną przez Ciebie pocztę lub na kilka różnych kont, a następnie
sprawdzi czy są tam nowe wiadomości.
Jeśli tak, to powinno być możliwe ich pobranie/usunięcie.
Program powinien mieć także możliwość wyszukiwania maila na
podstawie wyrażenia regularnego i szukać go w jego temacie lub treści.

Konfiguracja klienta oraz przypisanych maili powinna być
zapisana w postaci pliku YML.'''
import email
from email.header import decode_header
import imaplib
import yaml
import argparse
import os, os.path
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='count', default=0)

# patern = input('Podaj tekst tematu maila do wyszukania')

try:
    args = parser.parse_args()
    if  args.verbose == 1: # -v
        with open('skrzynki.yaml', 'r') as file:
            data_yaml = yaml.safe_load_all(file)
            data_iter = iter(data_yaml)
            dict = next(data_iter)
            host = list(dict.items())[0][1]
            user = list(dict.items())[1][1]
            password = list(dict.items())[2][1]

            imap_server = imaplib.IMAP4_SSL(host)
            imap_server.login(user, password)
            imap_server.select('INBOX')
            message_ids = imap_server.search(None, 'ALL')
            # print('message_ids',message_ids)

            typ, data = message_ids

            for m in data[0].split()[-5:]:
                typ, data = imap_server.fetch(m, '(RFC822)')
                message = email.message_from_bytes(data[0][1])
                subject, subject_encoding = decode_header(message['Subject'])[0]
                print('subject', subject)
                try:
                    if subject_encoding is not None:
                        subject = subject.decode('utf-8')
                except UnicodeDecodeError:
                    print('Zle kodowanie')

                email_from, from_encoding = decode_header(message['From'])[0]
                try:
                    if from_encoding is not None:
                        email_from = email_from.decode('utf-8')
                except UnicodeDecodeError:
                    print('Zle kodowanie')

                print(subject, email_from)
                while True:
                    key = input('Nacisnij d jesli chcesz usunąć mail')
                    if key == 'd':
                        imap_server.store(m, '+FLAGS', '\\Deleted')
                    break
            imap_server.expunge()

    if args.verbose == 2: #
       pass
    if args.verbose == 0:
        print('default')
except:
    print('błąd parametrów')

