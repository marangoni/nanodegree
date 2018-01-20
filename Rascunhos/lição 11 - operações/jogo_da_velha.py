# Jogo da velha


current_positions = {"top left": " ", "top center": " ", "top right": " ",
             "center left": " ", "center": " ", "center right": " ",
             "bottom left": " ", "bottom center": " ", "bottom right": " "}

# Funcao para desenhar o tabuleiro
def display_board(current_positions):
    board = """
    {top left} | {top center} | {top right}
    ---------
    {center left} | {center} | {center right}
    ---------
    {bottom left} | {bottom center} | {bottom right}
    """.format(**current_positions)
    print board

display_board(current_positions)

# Funcao para possibilitar um movimento

def user_move(current_positions, current_player):
    "Let a human user make a move"
    #First, find which moves are possible to make
    possible_moves = []
    #We also need to prompt the user for what choices they can make
    user_prompt = "Please pick your move from the options below!"
    for position in current_positions:
        #It's only a possible move if the space both exists and is empty
        if current_positions[position] == " ":
            possible_moves.append(position)
            user_prompt += "\n" + position
    user_prompt += '\n'
    #since Python is case sensitive, we'll make sure to convert everything
    #the user gives to lower-case to avoid confusion with string.lower()
    user_choice = raw_input(user_prompt).lower()
    while user_choice not in possible_moves:
        user_choice = raw_input(user_prompt).lower()
    #Once we exit the loop, the user has chosen a legal next move

    #Time to update the dictionary based on the move just made
    current_positions[user_choice] = current_player

    #Now we update whose turn it is
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    #We return the current positions and whose turn it is
    return current_positions, current_player

# Verificacao se alguem ganhou o Jogo
def is_game_over(current_positions):
    #Assuming only one winner
    winners = [["top left", "top center", "top right"],
               ["center left", "center", "center right"],
               ["bottom left", "bottom center", "bottom right"],
               ["top left", "center left", "bottom left"],
               ["top center", "center", "bottom center"],
               ["top right", "center right", "bottom right"],
               ["top left", "center", "bottom right"],
               ["top right", "center", "bottom left"]]
    #Going through all of the winning combinations
    for winning_combo in winners:
        #Someone will only have possibly won if every entry is the same as the first
        possible_winner = current_positions[winning_combo[0]]

        #Nobody has won if any entry is " ", including the first
        if possible_winner != " ":
            possibly_won = True
            for value in winning_combo:
                if current_positions[value] != possible_winner:
                    possibly_won = False
                    break
            if possibly_won:
                return possible_winner + " Wins!"

    #If we get this far, that means that nobody has won
    #Test for a draw; are any spaces still " "?
    is_draw = True
    for position in current_positions:
        if current_positions[position] == " ":
            is_draw = False
            #Looks like we should continue the game!
            return False

    #Note; if we get this far, there is definitely a draw
    if is_draw:
        return "Draw!"

# Funcao para jogar o jogo!
def play_game():
    #Start by defining our variables so that we don't need to rely on globals
    current_positions = {"top left": " ", "top center": " ", "top right": " ",
             "center left": " ", "center": " ", "center right": " ",
             "bottom left": " ", "bottom center": " ", "bottom right": " "}
    current_player = "X"
    #Play while our is_game_over() function tells us the game isn't over
    result = False
    while not result:
        #Display the current board after every turn
        display_board(current_positions)
        #always update our positions and turns
        current_positions, current_player = user_move(current_positions, current_player)
        #always check to see if the game is over
        result = is_game_over(current_positions)
        if result:
            display_board(current_positions)
            print "GAME OVER"
            print "Result: ", result


play_game()
