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
        khan_percent = vote_count["Khan"]/len(total_votes)
        correy_percent = vote_count["Correy"]/len(total_votes)
        li_percent = vote_count["Li"]/len(total_votes)
        otooley_percent = vote_count["O'Tooley"]/len(total_votes)

# The total number of votes each candidate won

# The winner of the election based on popular vote.
        winner = max(vote_count.items(), key=operator.itemgetter(1))[0]

print (len(total_votes))
print (vote_count)
print (khan_percent)
print (correy_percent)
print (li_percent)
print (otooley_percent)
print (winner)
