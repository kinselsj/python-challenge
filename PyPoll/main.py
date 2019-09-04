import os
import csv
import operator

#Path to collect data
election_data = os.path.join('election_data.csv')

# Read in the CSV file
with open(election_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    total_votes = []
    vote_count = {}
    
    # Loop through the data
    for row in csvreader:
        candidates = row[2]

# The total number of votes cast
        total_votes.append(row[0])
# A complete list of candidates who received votes
        ch_new = candidates in vote_count.keys()
        if ch_new: 
            vote_count [candidates] += 1
        else: 
            vote_count [candidates] = 1
# The percentage of votes each candidate won
    khan_vote = vote_count["Khan"]
    khan_percent = '{percent:.3%}'.format(percent=khan_vote/len(total_votes))
    correy_vote = vote_count["Correy"]
    correy_percent = '{percent:.3%}'.format(percent=correy_vote/len(total_votes))
    li_vote = vote_count["Li"]
    li_percent = '{percent:.3%}'.format(percent=li_vote/len(total_votes))
    otooley_vote = vote_count["O'Tooley"]
    otooley_percent = '{percent:.3%}'.format(percent=otooley_vote/len(total_votes))

# The total number of votes each candidate won

# The winner of the election based on popular vote.
    winner = max(vote_count.items(), key=operator.itemgetter(1))[0]

print ("Election Results")
print ("-----------------------")
print (f"Total Votes: {len(total_votes)}")
print ("-----------------------")
print (f"Khan: {khan_percent} ({khan_vote})")
print (f"Correy: {correy_percent} ({correy_vote})")
print (f"Li: {li_percent} ({li_vote})")
print (f"O'Tooley: {otooley_percent} ({otooley_vote})")
print ("-----------------------")
print (f"winner: {winner}")
print ("-----------------------")
