import csv, os
from pprint import pprint

# Set path to the target csv file
dirname = os.path.dirname(__file__)
election_csv = os.path.join(dirname, 'Resources\\election_data.csv')



# Send this csv to a dictionary to allow for summing by grouped values
# source code [5]: https://stackoverflow.com/questions/20200433/convert-csv-table-to-dictionary
def election_results(election_csv):
    csvreader = csv.DictReader(open(election_csv))
    rows = [r for r in csvreader]
    # print(rows)

    # get list of all ballot IDs then len() to get Total Votes
    ballots = [d['Ballot ID'] for d in rows]
    total_votes = len(ballots)
    print(f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------")

    # get unique candidates for looping through list for individual candidate count
    # source code: https://www.scaler.com/topics/convert-list-to-set-python/
    candidates = [c['Candidate'] for c in rows]
    unique_candidates = set(candidates)
    # print(unique_candidates)

    # # loop through unique candidates and candidates lists to get count of votes per candidate
      # set variable to sum votes by unique candidate
    winner_total = 0
    winner = 0
    for uc in unique_candidates:
        total = 0

        for c in candidates:
            if uc == c:
                total += 1

        if total > winner_total:
            winner_total = total
            winner = uc

        percent_vote = "{:.3f}".format((total/total_votes)*100) #formatting source: https://stackoverflow.com/questions/6149006/how-to-display-a-float-with-two-decimal-places
        # print(total)

        # print(percent_vote + "%")
        print(f"{uc}: {percent_vote}% ({total})")
        
    print("-------------------------")
    print(f"Winner: {winner}\n-------------------------\n")

election_results(election_csv)