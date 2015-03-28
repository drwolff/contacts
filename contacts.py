import csv
import random
import string


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

with open('test.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    title=['First Name','Mobile Phone']
    a.writerow(title)

with open('test.csv', 'a', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    for x in range(12142000000,12149999999):
        contact=[random_char(10),x]
        a.writerow(contact)

with open('test.csv', 'a', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    for x in range(14692000000,14699999999):
        contact=[random_char(10),x]
        a.writerow(contact)

with open('test.csv', 'a', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    for x in range(19722000000,19729999999):
        contact=[random_char(10),x]
        a.writerow(contact)
