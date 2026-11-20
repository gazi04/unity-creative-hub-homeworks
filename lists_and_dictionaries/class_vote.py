candidates = ["Python", "SQL", "Excel", "Power BI"]
votes = [
    "Python",
    "SQL",
    "Python",
    "Excel",
    "SQL",
    "Java",
    "Python",
    "Power BI",
    "SQL",
    "",
    "Python",
    "Excel",
    "SQL",
    "SQL",
    "Python",
    "SQL",
]

results = {c: 0 for c in candidates}
invalid_votes = 0

for v in votes:
    if v in candidates:
        results[v] += 1
    else:
        invalid_votes += 1

winner = ""
winner_votes = 0
print("===== CLASS VOTE =====")
for candidate, count in results.items():
    print(f"{candidate}: {'#' * count} ({count})")
    if count > winner_votes:
        winner = candidate
        winner_votes = count
print("----------------------")

candidates_with_max = 0
for candidate, count in results.items():
    if count == winner_votes:
        candidates_with_max += 1


valid_votes = len(votes) - invalid_votes
winner_percentage = (winner_votes / valid_votes) * 100

print("Total votes:", len(votes))
print("Valid votes:", valid_votes)
print("Invalid votes:", invalid_votes)

if candidates_with_max > 1:
    print(f"It's a tie! {candidates_with_max} candidates have {winner_votes} votes")
else:
    print(f"Winner: {winner} with {winner_votes} votes ({winner_percentage:.1f}%)")
print("======================")
