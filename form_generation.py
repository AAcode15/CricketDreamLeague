import csv

team1 = input('Team 1:')
team2 = input('Team 2:')

form_gen_file = open('form_gen.txt' , 'w')
League_data_file = open('League_data.csv')
player_reader = csv.DictReader(League_data_file)
for row in player_reader:
    if row['Team'] == team1 or row['Team'] == team2:
         form_gen_file.write(row['Player'] +  '  Creds: '+ str(row['Credit'] + '  Team: ' + row['Team'] +'\n'))
form_gen_file.close()
League_data_file.close()
