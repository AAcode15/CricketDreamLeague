import csv
class Player():
    def __init__(self, name, credit, team, points=0):
        self.name = name
        self.credit = int(credit)
        self.team = team
        self.points = float(points)

    def __repr__(self):
        return self.name+str(self.credit)

    def update_points(self, i):
        self.points += float(i)

class Participant():
    def __init__(self, name, id, team_dict, team_points = 0):
        self.id = id
        self.name = name
        self.cap = team_dict['Captain']
        self.vc = team_dict['Vice Captain']
        self.p3 = team_dict['Player 3']
        self.p4 = team_dict['Player 4']
        self.p5 = team_dict['Player 5']
        self.p6 = team_dict['Player 6']
        self.p7 = team_dict['Player 7']
        self.team_points = team_points

    def __repr__(self):
        return self.name+' '+self.id

    def calculator(self):
        self.team_points = self.cap.points * 2
        self.team_points += self.vc.points * 1.5
        self.team_points += self.p3.points + self.p4.points + self.p5.points + self.p6.points + self.p7.points

teams_list = {}
#reading ids and names
match_number = input('Match Number:')
ids = []
names = []
filename_part = 'participants_' + str(match_number)
participant_data = open('%s.csv' %filename_part)
id_reader = csv.DictReader(participant_data)
for row in id_reader:
    ids.append(int(row['ID']))
    names.append(row['Name'])
id_names = dict(zip(ids,names))
#print(id_names)

#reading match players and credits
team1 = input('Team 1:')
team2 = input('Team 2:')

player_list = {}
League_data_file = open('League_data.csv')
player_reader = csv.DictReader(League_data_file)
for row in player_reader:
    if row['Team'] == team1 or row['Team'] == team2:
         player_list[row['Player']] = (Player(row['Player'],row['Credit'],row['Team']))

print(player_list)


#verifying and storing participant teams
filename = 'participant_data_match_' + str(match_number)
participant_match_data = open('%s.csv' %filename)
participant_reader = csv.DictReader(participant_match_data)
participant_list = []
error_list = []
current_list = []
for participant in participant_reader:
    #print(participant)
    if not participant['ID'].isdigit():
        error_list.append(participant['ID'])
        continue
    if int(participant['ID'])  not in ids:
        error_list.append(participant['ID'])
        continue
    if int(participant['ID']) in current_list:
        error_list.append(str(participant['ID']) + ' DUP')
        continue
    current_list.append(int(participant['ID']))
    team_list = [participant['Captain'], participant['Vice Captain'], participant['Player 3'],  participant['Player 4'], participant['Player 5'], participant['Player 6'], participant['Player 7']]
    #print(team_list)
    team_list_names = []
    for plyr in team_list:
        plyr_split = plyr.split()
        #print(plyr, plyr_split)
        team_list_names.append(plyr_split[0])
    #print(team_list_names)
    team_set = set(team_list_names)
    if len(team_list_names) != len(team_set):
        error_list.append(str(participant['ID']) + ' DUP plyr')
        current_list.remove(int(participant['ID']))
        continue
    i = 1
    team = {}
    count_team = 0
    credits = 0
    for plyr in team_list_names:
        if i == 1:
            team['Captain'] = player_list[plyr]
        elif i == 2:
            team['Vice Captain'] = player_list[plyr]
        else:
            team['Player ' + str(i)] = player_list[plyr]
        i += 1
        curr_player = player_list[plyr]
        credits += curr_player.credit
        if curr_player.team == team1:
            count_team += 1

    if credits > 900:
        error_list.append(str(participant['ID']) + ' Excess Credits Used')
        current_list.remove(int(participant['ID']))
        continue
    if count_team<3 or count_team>4:
        error_list.append(str(participant['ID']) + ' team compostion mismatch')
        current_list.remove(int(participant['ID']))
        continue

    teams_list[int(participant['ID'])] = Participant(id_names[int(participant['ID'])], int(participant['ID']), team)


    print(team)
    print(credits)

print(current_list)
print(error_list)

for p in teams_list.values():
    p.calculator()
    i = 0
    p_list = []
    p_list.append(p.name)
    while i < 7:
        if i == 0:
            p_list.append((p.cap.points * 2.0))
            i += 1
        if i == 1:
            p_list.append((p.vc.points * 1.5))
            i += 1
        if i == 2:
            p_list.append(p.p3.points)
            i += 1
        if i == 2:
            p_list.append(p.p3.points)
            i += 1
        if i == 3:
            p_list.append(p.p3.points)
            i += 1
        if i == 4:
            p_list.append(p.p3.points)
            i += 1
        if i == 5:
            p_list.append(p.p3.points)
            i += 1
        if i == 6:
            p_list.append(p.p3.points)
            i += 1
    p_file_name = p.name + str(match_number)
    p_file = open('%s.txt' %p_file_name, 'w')
    p_file.write(p.cap.name + ' ' + str(p.cap.points * 2.0 ) + '\n' + p.vc.name + ' ' + str(p.vc.points * 1.5 ) + '\n' + p.p3.name + ' ' + str(p.p3.points) + '\n' + p.p4.name + ' ' + str(p.p4.points) + '\n' + p.p5.name + ' ' + str(p.p5.points) + '\n' + p.p6.name + ' ' + str(p.p6.points) + '\n' + p.p7.name + ' ' + str(p.p7.points) + '\n')
    p_file.close()
