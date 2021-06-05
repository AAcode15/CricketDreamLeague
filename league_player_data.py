import csv

Player_dict = [{'Player' : 'anuj', 'Team' : 'kaaleen', 'Credit' : 250}, {'Player' : 'nitin', 'Team' : 'kaaleen', 'Credit' : 95}, {'Player' : 'charchit', 'Team' : 'kaaleen', 'Credit' : 160}, {'Player' : 'madhu', 'Team' : 'kaaleen', 'Credit' : 140}, {'Player' : 'rishavA', 'Team' : 'kaaleen', 'Credit' : 65}, {'Player' : 'anubhav', 'Team' : 'kaaleen', 'Credit' : 45}, {'Player' : 'jitesh', 'Team' : 'kaaleen', 'Credit' : 140}, {'Player' : 'rishavG', 'Team' : 'munna', 'Credit' : 250}, {'Player' : 'mridul', 'Team' : 'munna', 'Credit' : 180}, {'Player' : 'aman', 'Team' : 'munna', 'Credit' : 70}, {'Player' : 'nilay', 'Team' : 'munna', 'Credit' : 240}, {'Player' : 'harsh', 'Team' : 'munna', 'Credit' : 160}, {'Player' : 'akshat', 'Team' : 'munna', 'Credit' : 20}, {'Player' : 'divyang', 'Team' : 'munna', 'Credit' : 30}, {'Player' : 'shivam', 'Team' : 'guddu', 'Credit' : 250}, {'Player' : 'krishna', 'Team' : 'guddu', 'Credit' : 160}, {'Player' : 'shreyansh', 'Team' : 'guddu', 'Credit' : 65}, {'Player' : 'pushpak', 'Team' : 'guddu', 'Credit' : 55}, {'Player' : 'akhil', 'Team' : 'guddu', 'Credit' : 20}, {'Player' : 'pratham', 'Team' : 'guddu', 'Credit' : 45}, {'Player' : 'harshit', 'Team' : 'guddu', 'Credit' : 190}, {'Player' : 'ankit', 'Team' : 'bablu', 'Credit' : 250}, {'Player' : 'tanay', 'Team' : 'bablu', 'Credit' : 25}, {'Player' : 'adarsh', 'Team' : 'bablu', 'Credit' : 90}, {'Player' : 'vedant', 'Team' : 'bablu', 'Credit' : 100}, {'Player' : 'naitik', 'Team' : 'bablu', 'Credit' : 150}, {'Player' : 'gaurav', 'Team' : 'bablu', 'Credit' : 200}, {'Player' : 'shubham', 'Team' : 'bablu', 'Credit' : 35}]

fields = ['Player' , 'Team', 'Credit']

with open('League_data.csv' , 'w') as League_data_file:
    file_writer = csv.DictWriter(League_data_file, fieldnames = fields)

    file_writer.writeheader()
    for item in Player_dict:
        file_writer.writerow(item)
