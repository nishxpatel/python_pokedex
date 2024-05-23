Simple Pokédex

Overview

This project is a simple Pokédex program that allows users to interact with a database of Pokémon, view details of individual Pokémon, and compare different Pokémon based on their names and statistics. The project consists of two main files:

1. pokedex.py: Defines the Pokémon class with methods for managing Pokémon data.
2. main.py: Provides a command-line interface for interacting with the Pokémon database.

Files

1. pokedex.py

Program: Simple Pokédex Class
Purpose: A program to interact with a database of Pokémon, allowing users to view details and compare different Pokémon.
Author: Nish Patel
Date: April 30, 2024

Pokémon Class

The Pokémon class represents a Pokémon with its attributes and methods. Key features include:

- Initialization: Create a Pokémon instance with its Pokedex number, name, types, and base stats.
- String Representation: Methods to provide readable string representations for display and debugging.
- Comparison Methods: Overloaded operators to compare Pokémon based on their total stats.
- Properties: Getters for Pokémon's number, name, types, stats, and total stats.
- Stat Retrieval: Method to get a specific stat by name.
- Data Loading: Class method to load Pokémon data from a file.
- Details Retrieval: Class method to get Pokémon details by name or Pokedex number.

2. main.py

Program: Simple Pokédex Main
Purpose: A program to interact with a database of Pokémon, allowing users to view details and compare different Pokémon.
Author: Nish Patel
Date: April 30, 2024

Main Functions

- Load Data: Load Pokémon data from a file using the Pokémon class method.
- Display Pokémon Details: Print detailed information about a Pokémon, including its stats.
- Compare Pokémon: Compare two Pokémon and print the comparison result based on their names.
- Main Interaction Loop: Command-line interface allowing users to:
  - Enter a Pokémon name or number to view its details.
  - Compare two Pokémon.
  - Exit the program.

How to Use

1. Ensure Data File Exists: Make sure the all_pokémon.txt file (or your specified file) containing Pokémon data is in the same directory as the scripts.
2. Run the Program: Execute main.py to start the command-line interface.
   python main.py
3. Follow Prompts: Enter a Pokémon name or number when prompted to view details or compare different Pokémon.

Example Usage

1. Viewing Pokémon Details:
   - Enter the name or number of a Pokémon to see its details.
   - Example: Enter a Pokémon name/number ("c" to exit): pikachu

2. Comparing Pokémon:
   - After viewing a Pokémon's details, choose to compare it to another Pokémon.
   - Example: Enter a Pokémon name/number to compare to Pikachu: charmander

3. Exiting the Program:
   - Enter c when prompted to exit the program.

Requirements

- Python 3.x

Contact

For any questions or issues, please contact Nish Patel.
