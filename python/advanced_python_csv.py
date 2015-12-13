## Advanced Python - writing to CSV
## Ozzie Liu
## Metis Pre-work

## Import functions from regex file to import and find list of email addresses
from advanced_python_regex import read_data, search_for_email
import csv

## Create faculty data file and email list
faculty = read_data('faculty.csv')
email_list = search_for_email(faculty)

## Open a CSV writer for emails.csv file
with open('emails.csv', 'wb') as csvtarget:
    email_writer = csv.writer(csvtarget, dialect = 'excel')

    ## Write each email address in its own row by iterating through emails
    ## and making each one a list.
    for email in email_list:
        email_writer.writerow([email])
