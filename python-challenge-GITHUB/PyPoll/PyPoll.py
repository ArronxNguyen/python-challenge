import os
import csv


#Set the path containing CSV file
csvpath = os.path.join('Resources','PyPoll_Resources_election_data.csv')


# integer variables
total_votes = 0
vote_count = 0
#string variables
candidate = ""
candidate_percent = ""
winner = ""
#list variables
all_candidates = []
vote_tally = []
vote_percentage = []


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
         # Read the header row first
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        # Count all the Vote ID 
        # every row after vote ID is a vote         
        if row[0] == 'Voter ID':
            pass
        else:
             vote_count = vote_count + 1
        # check all candidates to see if the name is in all candidates list
        if row[2] not in all_candidates:
        # if new candidate, add to candidate list using append and to vote tally
                all_candidates.append(row[2])
                vote_tally.append(1)    
        else:            
            vote_tally[all_candidates.index(row[2])] += 1


# sum up all the votes
total_votes = total_votes + vote_count


# list comprehension
# Return the vote tally of the element with the specified value of each candidate
for x in all_candidates:
    print( x + ": " + str(vote_tally[all_candidates.index(x)]))


# Calculate percent of vote            
vote_percentage = [(100/total_votes) * x for x in vote_tally]
# list comprehension
# Return the percentage of the element with the specified value of each candidate
for x in all_candidates:
         print( x + ": " + "{:.2f}".format(vote_percentage[all_candidates.index(x)]))


# find the max value in vote tally and return the candidate from all candidates
winner = all_candidates[vote_tally.index(max(vote_tally))]


# Print the analysis     
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for x in all_candidates:
    print(x + ": " + "{:.2f}".format(vote_percentage[all_candidates.index(x)]) 
        + "% (" + str(vote_tally[all_candidates.index(x)]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")


# Print the analysis to a txt file
with open ("PyPoll_Analysis.txt","w") as PyPoll_Analysis:
    print("Election Results\n", file=PyPoll_Analysis)
    print("---------------------------", file=PyPoll_Analysis)
    print("Total Votes: " + str(total_votes), file=PyPoll_Analysis)
    print("---------------------------", file=PyPoll_Analysis)
    print("-------------------------", file=PyPoll_Analysis)
    for x in all_candidates:
        print(x + ": " + "{:.2f}".format(vote_percentage[all_candidates.index(x)]) 
        + "% (" + str(vote_tally[all_candidates.index(x)]) + ")", file=PyPoll_Analysis)
    print("-------------------------", file=PyPoll_Analysis)
    print("Winner: " + winner, file=PyPoll_Analysis)
    print("-------------------------", file=PyPoll_Analysis)





