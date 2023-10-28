from pathlib import Path

def _bad_file_message():
    print()
    print("WARNING: The file you are using is either empty or not in the expected format, NO WINNER COULD BE CHOSEN")
    print("Please confirm that the .csv file is correct format and has data in it before trying again")

def _file_not_found_message():
    print()
    print("ERROR!!!!! File not found. Check to make sure the file is named 'raffle.csv'.")
    print(f"If the file is correctly named, then check to make sure the file is in the same folder as this program. The pathname here is: {Path.cwd()}")
    print("Please check that both of these things are done correctly and try again")

def _bad_donation_message():
    print()
    print("ERROR!!! When trying to get the number of tickets from Donation Levels column, looks like there was issues reading that value")
    print("Please check values in that column and make sure they are all in expected format and try again!")

def _unexpected_donation_message():
    print()
    print("ERROR!!! When trying to get the number of tickets from Donation Levels column, looks like there was issues reading that value")
    print("I expect a number to be the first thing that shows up in that column but what I got is not a number")
    print("Please check values in that column and make sure they are all in expected format and try again!")
