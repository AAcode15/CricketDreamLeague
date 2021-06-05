# CricketDreamLeague

1. First open league_player_data in a text editor, edit the player names, teams and credit points for each player.

2. Run the league_player_data.py file to generate a file named 'League_data.csv'

3. Run the form_generation.py file. You will be prompted to enter the name of the two teams. A new file named form_gen.txt will be created.

4. Open browser and navigate to google forms website. Create form with drop down options for players from the form_gen.txt file. Share form with friends and explain them the rules for building a team as follows:
        a. Everyone must choose 7 players
        b. One can only choose maximum of 4 players from either of the teams
        c. One can only use a maximum of 900 credits to make team.
        d. they must obtain a id(unique identifier) from you, which they must enter at the given location in the google form.


5. Download the responses of the form in csv format. Rename the file as participants_data_match_1 (the last digit represents the match number, in this case 1)

6. Run participant_gen.py, enter match number, bet amount. Then enter the name on the participant and the unique id that you provided him. Once you are done entering the details for your participants you need to type exit. This will create a file participants_1.csv (the last digit represents the match number, in this case 1).

7. Now you can run the test_read.py file to check if the input from your participants is correct, incase the have made a mistake u can allow them to refill the form without errors. Remember to Download the responses again and rename the file as in step 5. Replace the old file with the new one.

8. Run the match.py file when a game starts. enter match number and the name of the two teams.
      Event code are as follows:
      'r' for runs or boundries
      'b' for bowled
      'c' for catch out
      's' for stump out
      'ro' for run out
      'ep' for points based on economy of Bowler (award at the end of match only)
      'sr' for points based on strike rate of batsman (award at the end of match only)
      'bonus' for awarding special points to player
      'sub' for reducing points of player
Enter 'exit' once all points have been awarded and match is over.  

9. Points that have been awarded based on events are as follows:
        runs: points for every run, +1 for hitting a boundary, +2 for hitting a six.
        wicket: +25 for every wicket(catch out, stump out, bowled/lbw), +8 extra for bowled/lbw, +8 to catcher, +12 to wicketkeeper for stumping.
        run out: +12 to fielder
        economy: +6 if below 5, +4 between 5-5.99, +2 between 6-7, -2 between 10-11, -4 between 11.01-12, -6 above 12.
        strike rate: +6 above 170, +4 between 150.01-170, +2 between 130-150, -2 between 60-70, -4 between 50-59.99, -6 below 50
        bonus: +4 for 3 wickets, +8 for 4 wickets, +16 for 5 wickets, +12 for maiden over, +4 for 3 catches, +4 for 30-49 runs, +8 for 50-99 runs, +16 for 100 runs or higher
        Sub: -2 for getting out in duck(0 runs)

        For participant team total points, the points of the player selected as captain is doubled, the points of the player selected as vice captain is 1.5 times, the rest 5 player points are added without modification. The participant with highest total wins

10. After step 8 is over, a file named match_1.csv (the last digit represents the match number, in this case 1) is created, which shows the participant name and their total points in descending order. A file for every participant is also generated, as (participantname)(matchnumber).txt, which shows the performance of the different players in their teams. The results can be declared based on the match_1.csv file.

 ------------------------thank you for your time----------------------------
