#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Relationship Status Problem

def relationship_status(from_member, to_member, social_graph):

    followers_from_member = list(social_graph[from_member]["following"])
    followers_to_member = list(social_graph[to_member]["following"])
    
    if to_member in followers_from_member and from_member in followers_to_member:
        return "friends"
    elif to_member in followers_from_member:
        return "follower"
    elif from_member in followers_to_member:
        return "followed by"
    else:
        return "no relationship"

# Tic Tac Toe Problem

def tic_tac_toe(board):

    size = len(board)

    for row in board:
        if all(cell == row[0] and cell != '' for cell in row):
            return row[0]
    
    for col in range(size):
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(size)):
            return board[0][col]
    
    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(size)):
        return board[0][0]
    
    if all(board[i][size - 1 - i] == board[0][size - 1] and board[i][size - 1 - i] != '' for i in range(size)):
        return board[0][size - 1]
        
    return "NO WINNER"

# Estimated Time of Arrival Problem

def eta(first_stop, second_stop, route_map):
    
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]
    
    current_stop = first_stop
    total_time = 0
    
    while current_stop != second_stop:
        found_next_stop = False
        for leg in route_map:
            if leg[0] == current_stop:
                next_stop = leg[1]
                total_time += route_map[leg]["travel_time_mins"]
                current_stop = next_stop
                found_next_stop = True
                break
        if not found_next_stop:
            break
    
    return total_time

