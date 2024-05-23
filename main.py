# Program: Simple Pokédex Main
# Purpose: A program to interact with a database of Pokémon,
#          allowing users to view details and compare different Pokémon.
# Author:  Nish Patel
# Date:    April 30, 2024

from pokedex import Pokémon

def load_data():
    """
    Load Pokémon data from the source.
    
    This function attempts to load Pokémon data using the `load_pokémon_data` method of the `Pokémon` class. 
    If an exception occurs during loading, it prints an error message.
    """
    try:
        Pokémon.load_pokémon_data()
    except Exception as e:
        print(f"Error loading Pokémon data: {e}")

def display_pokémon_details(pokémon):
    """
    Display details of a Pokémon.

    Args:
        pokémon (Pokémon): The Pokémon object to display details for.

    Prints the name, types, and stats of the given Pokémon.
    """
    print(f"\nPokémon:            {pokémon}")
    print(f"Types:              {pokémon.types}")
    print("Stats:")
    print(f"  HP:               {pokémon.stats[0]:>3}")
    print(f"  Attack:           {pokémon.stats[1]:>3}")
    print(f"  Defense:          {pokémon.stats[2]:>3}")
    print(f"  Special Attack:   {pokémon.stats[3]:>3}")
    print(f"  Special Defense:  {pokémon.stats[4]:>3}")
    print(f"  Speed:            {pokémon.stats[5]:>3}")
    print(f"  Total:            {pokémon.total:>3}\n")

def compare_pokémon(pokémon1, pokémon2):
    """
    Compare two Pokémon based on their total stats.

    Args:
        pokémon1 (Pokémon): The first Pokémon to compare.
        pokémon2 (Pokémon): The second Pokémon to compare.

    Prints a comparison result based on the total stats of the Pokémon.
    """
    if pokémon1 == pokémon2:
        print(f"{pokémon1}'s stat total is IDENTIAL to {pokémon2}'s stat total\n")
    elif pokémon1 > pokémon2:
        print(f"{pokémon1}'s stat total is GREATER than {pokémon2}' stat total\n")
    else:
        print(f"{pokémon1}'s stat total is LESSER than {pokémon2}' stat total\n")

def main():
    """
    Main function to interact with the Pokémon database.
    
    This function loads Pokémon data and allows the user to:
    - Enter a Pokémon name or number to view its details.
    - Compare two Pokémon based on their total stats.
    """
    load_data()

    while True:
        pokémon_name = input('Enter a Pokémon name/number ("c" to exit): ').strip().lower()
        if pokémon_name == 'c':
            print('Goodbye')
            break
        pokémon = Pokémon.get_pokémon_details(pokémon_name)

        if pokémon:
            display_pokémon_details(pokémon)

            while True:
                action = input(f"What would you like to do next? \n"
                               "a. See another Pokémon\n"
                               "b. Compare to another Pokémon\n"
                               "c. Quit\n\n").strip().lower()

                if action == 'a':
                    break
                elif action == 'b':
                    pokémon2_name = input(f"Enter a Pokémon name/number to compare to {pokémon}: ").strip().lower()
                    pokémon2 = Pokémon.get_pokémon_details(pokémon2_name)
                    if pokémon2:
                        display_pokémon_details(pokémon2)
                        compare_pokémon(pokémon, pokémon2)
                    else:
                        print("Pokémon not found!")
                elif action == 'c':
                    print('Goodbye')
                    return
                else:
                    print("Invalid choice. Please select a valid option.")

        else:
            print("Pokémon not found!")

if __name__ == "__main__":
    main()
