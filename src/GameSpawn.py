def game_spawn_logic(current_score):
    print(f"--- Player Score reached {current_score}! Analyzing spawns... ---")

    # We iterate through the points the player just earned
    # Let's say they just jumped from 0 to 100
    for point in range(1, current_score + 1):

        # Rule 1: Every 100 points (Big Event)
        if point % 100 == 0:
            print(f"SCORE {point}: !!! BOSS BATTLE STARTED !!!")

        # Rule 2: Every 25 points
        elif point % 25 == 0:
            print(f"SCORE {point}: [Alert] Heavy Tanker incoming!")

        # Rule 3: Every 10 points
        elif point % 10 == 0:
            print(f"SCORE {point}: Scout ship detected.")


# Simulate reaching a score of 100
game_spawn_logic(100)
