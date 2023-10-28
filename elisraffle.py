import csv
import random
import messages_from_above

def pick_raffle_winner(printout = True):

    '''
    Making sure the raffle ticket records file exists and can be read
    '''
    try:
        open('raffle.csv')
    except FileNotFoundError:
        messages_from_above._file_not_found_message()
        exit()

    '''
    Adding all of the tickets into the pot
    '''
    pot = list()
    with open('raffle.csv') as raffle_entries_file:
        entry_reader = csv.reader(raffle_entries_file, delimiter=",")
        tickets = [row for row in entry_reader]

        for row in tickets[1:]:
            '''
            Checks that each row has necessary information in it to add person's tickets.
            If row does not have value in 'name' and 'donation levels' columns, then it is considered to be the end of the entries.
            '''
            print(row)
            if row[2] == '' or row[4] == '':
                break
            try:
                num_tickets = _parse_number(row[4])
            except LookupError:
                messages_from_above._bad_donation_message()
                exit()
            except ValueError:
                messages_from_above._unexpected_donation_message()
                exit()

            for _ in range(num_tickets):
                pot.append(row[:4])

    '''
    If the file is read and there is nothing in the pot, it is assumed something is wrong. This lets user know.
    '''
    if not pot:
        messages_from_above._bad_file_message()
        exit()
    
    '''
    This picks a random number then uses that slot in the list as the winner
    '''
    lucky_number = random.randint(0,len(pot)-1)
    if printout:
        print(f"The big winner is: {pot[lucky_number]}")

    '''
    Anyone not named Elius can ignore this bottom line
    '''
    return pot[lucky_number][2]


def _parse_number(donation_level):
    '''
    Function to take in the strings in the 'Donation Levels' column of the spreadsheet and just get the number 
    of tickets someone bought from it.This function assumes the string is in the following format: 
    (integer number)+whitespace+(anything else) and all it looks at and returns in that integer number as the 
    correct data type
    '''
    my_list = donation_level.split()
    if not my_list:
        raise LookupError
    return int(my_list[0])

def _fairness_calculation(tally,plays):
    '''
    Small function I wrote to validate that my code was indeed fair and weighted apropriately
    '''
    for name,wins in tally.items():
        print(f"{name} has won {round(float(wins)/plays*100,2)}% of the time")


if __name__ == "__main__":
    '''
    This is the main function that gets called when the file is run. This is just an infinite loop where
    as long as the user keeps entering anything except an upper-case 'E' then the loop keeps looping. Within
    the loop it does keep track of the people that win and how many times they won. In practice this 
    shouldn't matter, but it validates the function of the code so you can go to bed tonight knowing this
    raffle was very official and fair.

    One thing to note is that in between each run, if the raffle.csv file is changed to moved, then the 
    subsequent run of the loop will pick up any changes made so that could be dangerous. Be careful out there!
    '''
    wins = dict()
    tries = 0
    user = "Y"
    while user != "E":
        winner = pick_raffle_winner()
        if winner not in wins:
            wins[winner] = 1
        else:
            wins[winner] += 1
        user = input("Press enter to run again or enter 'E' to exit: ")
        print()
        '''tries +=1
        if tries%10000 == 0:
            _fairness_calculation(wins, tries)
            input("Press enter to keep going")'''
        