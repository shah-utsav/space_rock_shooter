import random
import time
import os

# Define the game parameters
player_ship = "^"
width = 30
height = 20
score = 0
game_over = False

# Initialize the player's position
player_x = width // 2

# Initialize a list to store the rocks
rocks = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game():
    clear_screen()
    for row in range(height):
        row_str = ""
        for col in range(width):
            if row == 0 and col == player_x:
                row_str += player_ship
            elif (row, col) in rocks:
                row_str += "o"
            else:
                row_str += " "
        print(row_str)
    print(f"Score: {score}")

def move_rocks():
    new_rocks = []
    for rock in rocks:
        row, col = rock
        if row < height - 1:
            new_rocks.append((row + 1, col))
    return new_rocks

def generate_rock():
    col = random.randint(0, width - 1)
    return (0, col)

# Game loop
while not game_over:
    display_game()
    print("Press 'a' to move left, 'd' to move right, and 'q' to quit.")

    # Check if any rocks hit the player's ship
    for rock in rocks:
        if rock == (height - 1, player_x):
            game_over = True
            break

    if game_over:
        break

    user_input = input()
    if user_input == 'a' and player_x > 0:
        player_x -= 1
    elif user_input == 'd' and player_x < width - 1:
        player_x += 1
    elif user_input == 'q':
        game_over = True

    # Move and generate rocks
    rocks = move_rocks()
    if random.random() < 0.2:
        rocks.append(generate_rock())
    
    score += 1

    time.sleep(0.1)  # Add a slight delay for better gameplay

clear_screen()
print(f"Game over! Your final score is: {score}")
