from termcolor import colored

# Function to generate a Valentine's Day card
def generate_valentine_card(name, message, design="heart"):
    if design == "heart":
        # ASCII art of a heart
        art = '''
          ******       ******
       **********   **********
     ************* *************
    *****************************
    *****************************
     ***************************
       *************************
         *********************
           *****************
             *************
               *********
                 *****
                   *
        '''
    else:
        art = "Design not available."

    # Adding color to the text
    name_colored = colored(f"Dear {name},", 'red', attrs=['bold'])
    message_colored = colored(message, 'magenta')
    art_colored = colored(art, 'red')
    closing_colored = colored("With Love,\nYour Secret Admirer", 'blue', attrs=['bold'])

    # Creating the card with the user's input
    card = f'''
    {name_colored}
    
    {message_colored}
    
    {art_colored}
    
    {closing_colored}
    '''
    return card

# Example usage
name = "Alice"
message = "Wishing you a day filled with love and happiness! Happy Valentine's Day!"
# Print the generated card
print(generate_valentine_card(name, message, design="heart"))

