#  A light weight python program to get the count for candidate
# the length of the file is 803,000

import csv

my_file = "../GWDC201805DATA3-Class-Repository-DATA/03-Python/Resources/election_data.csv"
with open(my_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # To read the header from the csv file
    header = next(csvreader)
    #print(header)
     # intialize the vote count
    vote_count = 0
     # intialize and record candidate name
    candidate_name = []
     # intialize and record each candidate name and vote count 
    candidate_vote = {}
    # track the winner_vote
    wining_vote = 0
    # track wining candidate
    wining_candidate = ""
     
    for reader in csvreader:
        vote_count += 1
        candidate = reader[2]
        if candidate not in candidate_name:
            # In a way, this loop is "discovering" candidates as it goes and counts the vote while it starts counting 
            # the candidate vote
            candidate_name.append(candidate)
            candidate_vote[candidate] = 1
        else:
            candidate_vote[candidate] = candidate_vote[candidate] + 1
        
for row in candidate_vote:
    vote_per = candidate_vote.get(row)
    vote_percentage = vote_per/vote_count

    if vote_per > wining_vote:
        wining_vote = vote_per
        wining_candidate = row
        winner_percentage = wining_vote/vote_count
    print(row)
    print(vote_per)
    print(vote_percentage* 100,"%")
    print("-------------")
print("winner summary")
print(f'Winner :{wining_candidate}')
print(f'wining count : {wining_vote}')
print(f'wining percentage : {winner_percentage * 100}%')





    

        


              
