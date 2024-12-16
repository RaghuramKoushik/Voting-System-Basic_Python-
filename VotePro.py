print("\n\n================Voting System================\n\n")
voter_choice = []
symbols = ["!", "@", "#", "$", "%"]
part_choice = []

# Input for number of participants
part = int(input("Enter number of participants:\n"))
while True:
    if part > 1:
        break
    else:
        print("There must be at least two contesting candidates! Re-Conduct!")
        part = int(input("Enter number of participants:\n"))

# Input for participant symbols
for i in range(part):
    x = input(f"Choose symbol of participant {i + 1} from {symbols} \n")
    if x in symbols:
        part_choice.append(x)
        symbols.remove(x)
    else:
        print(f"{x} is an invalid choice! Please Re-Enter.")
        x = input(f"Choose symbol of participant {i + 1} from {symbols} \n")
        part_choice.append(x)
        symbols.remove(x)

print(part_choice, "are the symbols chosen by the participants.\n\n")

# Input for number of voters
while True:
    voters = int(input("Enter the total number of voters (at least 1):\n\n"))
    if voters > 0:
        break
    else:
        print("There must be at least one voter! Re-Conduct!")

# Initialize vote count for each participant
part_count = [0] * len(part_choice)

# Collect votes from voters
for i in range(voters):
    y = input(f"Enter voter {i + 1} choice from {part_choice}:\n")
    if y in part_choice:
        voter_choice.append(y)
        part_count[part_choice.index(y)] += 1
    else:
        print(f"{y} is an invalid choice! Please Re-Enter!\n")
        y = input(f"Enter voter {i + 1} choice from {part_choice}: ")
        voter_choice.append(y)
        part_count[part_choice.index(y)] += 1

# Display received votes
print("Votes received:", voter_choice)
print("\n\n")

# Check for tie condition
if 1 == max(part_count):
    print("All candidates have tied! Re-Conduct!")
    exit()

# Determine the winner and runner-up
max_vote1 = max(part_count)  # Highest vote count
winner1 = part_count.index(max_vote1)  # Index of the winner

part_count2 = part_count.copy()  # Copy to find second highest vote count
part_count2[winner1] = 0  # Set winner's count to zero to find next highest
max_vote2 = max(part_count2)  # Second highest vote count
winner2 = part_count2.index(max_vote2)  # Index of the runner-up

# Check for tie between top two candidates
if max_vote1 == max_vote2:
    print(f"Candidate {winner1 + 1} and candidate {winner2 + 1} have tied with {max_vote2} votes!")
else:
    if max_vote2 == 0:
        print(f"The winner is candidate {winner1 + 1} with {max_vote1} votes!\n")
    else:
        print(f"The winner is candidate {winner1 + 1} with {max_vote1} votes!\n")
        print(f"Their opposition will be candidate {winner2 + 1} with {max_vote2} votes!")

# Final candidate vote summary
print("\nFinal Candidate Vote Summary:")
for i in range(len(part_choice)):
    print(f"Candidate {i + 1} ({part_choice[i]}): {part_count[i]} votes")
