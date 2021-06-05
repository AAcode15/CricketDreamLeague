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


#funtions for points
def run_add(batsman, run):
    if int(run) == 4:
        batsman.update_points(5)
    elif int(run) == 6:
        batsman.update_points(8)
    else :
        batsman.update_points(run)

def bonus(plyr, bon):
    plyr.update_points(bon)

def ded(plyr, bon):
    b = float(bon) * -1
    plyr.update_points(b)

def catch(catcher, bowler):
    catcher.update_points(8)
    bowler.update_points(25)

def stumping(wicketkeeper, bowler):
    wicketkeeper.update_points(12)
    bowler.update_points(25)

def runout(fielder):
    fielder.update_points(12)

def bowled(bowler):
    bowler.update_points(33)

def economy_points(bowler,economy):
    if economy < 5:
        bowler.update_points(6)
    elif economy < 6:
        bowler.update_points(4)
    elif economy <= 7:
        bowler.update_points(2)
    elif economy >= 10 and economy <= 11:
        bowler.update_points(-2)
    elif economy > 11 and economy <= 12:
        bowler.update_points(-4)
    elif economy > 12:
        bowler.update_points(-6)

def strike_points(batsman, strike):
    if strike > 170:
        batsman.update_points(6)
    elif strike > 150:
        batsman.update_points(4)
    elif strike >= 130:
        batsman.update_points(2)
    elif strike >=60 and strike <=70:
        batsman.update_points(-2)
    elif strike >= 50 and strike < 60:
        batsman.update_points(-4)
    elif strike < 50:
        batsman.update_points(-6)

def plyr_input():
    p_name = input(' ')
    if p_name in player_list:
        plyr = player_list[p_name]
        return plyr
    else:
        print('wrong input')
        return None

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except:
        return False

def updator():
    match_list = []
    for p in teams_list.values():
        p.calculator()
        match_list.append({'Name': p.name, 'Points': p.team_points})
    match_list_sorted = sorted(match_list, key = lambda i: i['Points'], reverse = True)
    head = ['Name', 'Points']
    name_file = 'match_' + str(match_number)
    match_ranking = open('%s.csv' %name_file, 'w')
    rank_writer = csv.DictWriter(match_ranking, fieldnames = head )
    rank_writer.writeheader()
    for team in match_list_sorted:
        rank_writer.writerow(team)
    match_ranking.close()

#calling functions

while True:
    inp = input('Event Code:')
    if inp == 'r':
        print('Enter Batsman:')
        plyr = plyr_input()
        if plyr == None:
            continue
        run = input('runs:')
        if not run.isdigit():
            print('wrong input')
            continue
        run_add(plyr, run)
        updator()
        continue
    if inp == 'bonus':
        print('Enter Player:')
        plyr = plyr_input()
        if plyr == None:
            continue
        bon = input('Bonus:')
        if not bon.isdigit():
            print('wrong input')
            continue
        bonus(plyr, bon)
        updator()
        continue
    if inp == 'ded':
        print('Enter Player:')
        plyr = plyr_input()
        if plyr == None:
            continue
        bon = input('Bonus:')
        if not bon.isdigit():
            print('wrong input')
            continue
        ded(plyr, bon)
        updator()
        continue
    if inp == 'c':
        print('Enter Catcher:')
        plyr1 = plyr_input()
        if plyr1 == None:
            continue
        print('Enter Bowler:')
        plyr2 = plyr_input()
        if plyr2 == None:
            continue
        catch(plyr1, plyr2)
        updator()
        continue
    if inp == 's':
        print('Enter WK:')
        plyr1 = plyr_input()
        if plyr1 == None:
            continue
        print('Enter bowler:')
        plyr2 = plyr_input()
        if plyr2 == None:
            continue
        stumping(plyr1, plyr2)
        updator()
        continue
    if inp == 'ro':
        print('Enter Fielder:')
        plyr = plyr_input()
        if plyr == None:
            continue
        runout(plyr)
        updator()
        continue
    if inp == 'b':
        print('Enter Bowler:')
        plyr = plyr_input()
        if plyr == None:
            continue
        bowled(plyr)
        updator()
        continue
    if inp == 'ep':
        print('Enter Player:')
        plyr = plyr_input()
        if plyr == None:
            continue
        economy = input('Economy:')
        if not check_float(economy):
            print('wrong input')
            continue
        economy_points(plyr, float(economy))
        updator()
        continue
    if inp == 'sr':
        print('Enter Player:')
        plyr = plyr_input()
        if plyr == None:
            continue
        strike = input('strike rate:')
        if not check_float(strike):
            print('wrong input')
            continue
        strike_points(plyr, float(strike))
        updator()
        continue
    if inp == 'exit':
        break


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
