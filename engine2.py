import chess_lib as cl
import chess 
import opening_database  
import opening_search 
import time
import random
import timeit
import chess.polyglot
import random as rand
random.seed()

game_vars = {
    "board": False,
    "in_opening": True,
    "in_opening_book": True,
    "in_mid_game": False,
    "in_end_game": False,
    "opening_move": None,
    "opening_type": None,
    "debug_mode": False,
    "game": None,
    "is_check": False,
    "pieces": [[],[]],
    "check_mate": False,
    "start_depth": 3,
    "positions_ran": 0,
    "zobrist_keys": None
}

played_moves = []

def pawn_structure(board, color):
    pass

def material(board, color):
    pass

def endgame_strat(board, color):
    pass

def eval(board, depth):
    pass

def pre_compute(board, depth):
    pass

def negamax(board, depth, alpha, beta):
    pass

def run(last_move, board):
    move = None
    #pre_compute(board)
    time_begin = time.perf_counter()
    
    if len(opening_search.opening_moves) > 12:
        game_vars["in_opening"] = False
        
    #runs opening database and exits when its out of the opening.
    if game_vars["in_opening_book"]:
        book_move = opening_search.main_opening_search(last_move)
        if book_move:
            move = book_move.move
        if not move:
            game_vars["in_opening_book"] = False

    return move