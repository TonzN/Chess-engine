import chess_lib as cl
import chess 
import opening_database
import random as rand

engine_opening_preferences = {
    "e2e4": {
        opening_database.Ruy_lopez,
        opening_database.vienna_game
    },
    "d2d4": {
        opening_database.queens_gambit
    }
}

opening_vars = {
    "opening_move": False
}

opening_moves = []

debug_mode = False

def main_opening_search(last_move):
    opening_moves.append(last_move)
    if not opening_vars["opening_move"]:
        opening_vars["opening_move"] = last_move  
        #preference opening search
        if opening_vars["opening_move"] in engine_opening_preferences:   
            opening_vars["opening_type"] = opening_database[opening_vars["opening_move"]]       
        elif opening_vars["opening_move"] in opening_database:
            pass
        else:
            print("\nopening not in database, starts engine") 
            
    #debug....
    if debug_mode:
        print("\n",last_move)
    if opening_vars["opening_type"] == None:
        if debug_mode:
            print("\nError, no openingtype")
        return
        
    #main_search
    opening_type = opening_vars["opening_type"]
    available_moves = []
    for opening in opening_type: 
        if debug_mode:
            print(opening_type[opening].name)
            
        opening = opening_type[opening].root
        next_move = opening
        selected_move = None
        #search
        for i in opening_moves:
            if i in next_move.children:
                if len(next_move.children) > 1:
                    next_move = next_move.children[rand.choice(next_move.children)] #random opening variation
                else:
                    next_move = next_move.children[i]
                    selected_move = next_move
            else:
                selected_move = None
                next_move = None
                break
        
        if selected_move:
            available_moves.append(selected_move)
        
        if debug_mode:
            print("\nAvailable legal moves", available_moves)
    
    if len(available_moves) < 1: #didnt find any opening move
        return
    
    selected_move = rand.choice(available_moves)
    
    if selected_move: #double check so it doesnt select a move already played.
        if selected_move.move == last_move:
            selected_move = None
            if debug_mode:
                print("chose last move!!")
        else:
            opening_moves.append(selected_move.move)
            
    return selected_move #selected uci move