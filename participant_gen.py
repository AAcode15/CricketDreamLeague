import csv

number = input('Match number:')
bet_amount = input('Enter bet amount:')
participant_data = []
i = 1
while i != 0:
    name = input('Name:')
    if name == 'exit':
        break
    id = input('ID:')
    participant_data.append({'Name':name, 'ID':id, 'Bet': bet_amount})

fields = ['Name', 'ID', 'Bet']
filename = 'participants_' + str(number)
participants = open('%s.csv' %filename, 'w')
part_writer = csv.DictWriter(participants, fieldnames = fields)
part_writer.writeheader()
for part in participant_data:
    part_writer.writerow(part)
