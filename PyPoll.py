# Set up dependencies
import os
import csv

# Read in CSV file
election_data = os.path.join("Resources","election_data.csv")
os.path.join("Resources","election_data.csv")

# Sets up output file
output_file = os.path.join("Resources","election_data_output.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Reading csv file & declares variables
with open(election_data) as elec_data:
    reader = csv.reader(elec_data)
    header = next(reader)
    
    first_row = next(reader)
    
    total_votes = 0
    total_votes = total_votes +1
        
    can_1_percent = 0
    can_2_percent = 0
    can_3_percent = 0
    
    can_1_votes = 0
    can_2_votes = 0
    can_3_votes = 0

    # Loops through rows in reader for vote count and candidate name
    for row in reader:
        total_votes += 1
        if row[2] == ("Charles Casper Stockham"):
           can_name_1 = row[2]
           can_1_votes = can_1_votes + 1
           can_1_percent = can_1_votes / total_votes
           
        if row[2] == ("Diana DeGette"):
            can_name_2 = row[2]
            can_2_votes = can_2_votes + 1
            can_2_percent = can_2_votes / total_votes
                
        if row[2] == ("Raymon Anthony Doane"):
            can_name_3 = row[2]
            can_3_votes = can_3_votes + 1
            can_3_percent = can_3_votes / total_votes

            # Uses loop totals to output election winner
            if can_1_percent > can_2_percent and can_1_percent > can_3_percent:
                outcome = ("Winner: Charles Casper Stockham")

            elif can_2_percent > can_1_percent and can_2_percent > can_3_percent:
                outcome = ("Winner: Diana DeGette")

            elif can_3_percent > can_1_percent and can_3_percent > can_2_percent:
                outcome = ("Winner: Raymon Anthony Doane")

# Terminal output          
print("\n"
    f"Election Results\n" 
    f"--------------------------\n"
    f"Total Votes: {total_votes} votes\n"
    f"--------------------------\n"
    f"{can_name_1}: {round(can_1_percent,2)}% ({can_1_votes} votes)\n"
    f"{can_name_2}: {round(can_2_percent,2)}% ({can_2_votes} votes)\n"
    f"{can_name_3}: {round(can_3_percent,2)}% ({can_3_votes} votes)\n"
    f"--------------------------\n"
    f"{outcome}\n"
    f"--------------------------\n"
    )

# Text file output
output = (
    f"--------------------------\n"
    f"Election Results\n" 
    f"--------------------------\n"
    f"Total Votes: {total_votes} votes\n"
    f"--------------------------\n"
    f"{can_name_1}: {round(can_1_percent,2)}% ({can_1_votes} votes)\n"
    f"{can_name_2}: {round(can_2_percent,2)}% ({can_2_votes} votes)\n"
    f"{can_name_3}: {round(can_3_percent,2)}% ({can_3_votes} votes)\n"
    f"--------------------------\n"
    f"{outcome}\n"    
    f"--------------------------\n"
        )
with open(output_file, "w") as txt_file:
    txt_file.write(output)

