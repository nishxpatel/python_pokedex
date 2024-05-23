class Pokémon:
    """A class representing a Pokémon with its attributes and methods."""

    __pokémon_data = {}

    def __init__(self, number: int, name: str, types: list[str], stats: tuple[int, int, int, int, int, int]):
        """
        Initializes a Pokémon instance.

        Args:
            number (int): The Pokedex number of the Pokémon.
            name (str): The name of the Pokémon.
            types (list of str): The types of the Pokémon.
            stats (tuple of int): The base stats of the Pokémon.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        if not isinstance(number, int):
            raise ValueError("number must be an integer")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not all(isinstance(t, str) for t in types) or not (1 <= len(types) <= 2):
            raise ValueError("types must be a list of one or two strings")
        if not all(isinstance(stat, int) for stat in stats) or len(stats) != 6:
            raise ValueError("stats must be a tuple of six integers")

        self.__number = number
        self.__name = name
        self.__types = types
        self.__stats = stats
        self.__total = sum(stats)

    def __str__(self) -> str:
        """
        Returns a string representation of the Pokémon.

        Returns:
            str: A formatted string representation of the Pokémon's name and number.
        """
        return f"{self.__name.capitalize()} (#{self.__number})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Pokémon for debugging purposes.

        Returns:
            str: A string representation of the Pokémon.
        """
        return f"Pokémon({self.__number}, '{self.__name}', {self.__types}, {self.__stats})"

    def __eq__(self, other) -> bool:
        """
        Checks if two Pokémon instances are equal based on their total stats.

        Args:
            other (Pokémon): The other Pokémon to compare.

        Returns:
            bool: True if the total stats of both Pokémon are equal, False otherwise.
        """
        return self.__total == other.__total

    def __ne__(self, other) -> bool:
        """
        Checks if two Pokémon instances are not equal based on their total stats.

        Args:
            other (Pokémon): The other Pokémon to compare.

        Returns:
            bool: True if the total stats of both Pokémon are not equal, False otherwise.
        """
        return self.__total != other.__total

    def __lt__(self, other) -> bool:
        """
        Checks if one Pokémon instance has less total stats than the other.

        Args:
            other (Pokémon): The other Pokémon to compare.

        Returns:
            bool: True if this Pokémon's total stats are less than the other's, False otherwise.
        """
        return self.__total < other.__total

    def __le__(self, other) -> bool:
        """
        Checks if one Pokémon instance has less or equal total stats than the other.

        Args:
            other (Pokémon): The other Pokémon to compare.

        Returns:
            bool: True if this Pokémon's total stats are less than or equal to the other's, False otherwise.
        """
        return self.__total <= other.__total

    def __gt__(self, other) -> bool:
        """
        Checks if one Pokémon instance has greater total stats than the other.

        Args:
            other (Pokémon): The other Pokémon to compare.

        Returns:
            bool: True if this Pokémon's total stats are greater than the other's, False otherwise.
        """
        return self.__total > other.__total

    def __ge__(self, other) -> bool:
        """
        Checks if one Pokémon instance has greater or equal total stats than the other.

        Args:
            other (Pokémon): The other Pokémon to compare.

        Returns:
            bool: True if this Pokémon's total stats are greater than or equal to the other's, False otherwise.
        """
        return self.__total >= other.__total

    @property
    def number(self) -> int:
        """
        Getter for the Pokedex number of the Pokémon.

        Returns:
            int: The Pokedex number of the Pokémon.
        """
        return self.__number

    @property
    def name(self) -> str:
        """
        Getter for the name of the Pokémon.

        Returns:
            str: The name of the Pokémon.
        """
        return self.__name

    @property
    def types(self) -> str:
        """
        Getter for the types of the Pokémon.

        Returns:
            str: The types of the Pokémon, separated by commas if there are two types.
        """
        return ", ".join(self.__types)

    @property
    def stats(self) -> tuple[int, int, int, int, int, int]:
        """
        Getter for the base stats of the Pokémon.

        Returns:
            tuple of int: The base stats of the Pokémon.
        """
        return self.__stats

    @property
    def total(self) -> int:
        """
        Getter for the total sum of the base stats of the Pokémon.

        Returns:
            int: The total sum of the base stats of the Pokémon.
        """
        return self.__total

    def get_stat(self, stat_name: str) -> int:
        """
        Gets the value of a specific stat of the Pokémon.

        Args:
            stat_name (str): The name of the stat to retrieve.

        Returns:
            int: The value of the specified stat.

        Raises:
            ValueError: If an invalid stat name is provided.
        """
        stat_names = ['hp', 'attack', 'defense', 'sp. attack', 'sp. defense', 'speed']
        if stat_name.lower() in stat_names:
            index = stat_names.index(stat_name.lower())
            return self.__stats[index]
        else:
            raise ValueError(f"Invalid stat name: {stat_name}")

    @classmethod
    def load_pokémon_data(cls, filename: str = 'all_pokémon.txt'):
        """
        Loads Pokémon data from a file and initializes Pokémon instances.

        Args:
            filename (str): The name of the file containing Pokémon data.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file contents are not properly formatted.
        """
        try:
            with open(filename, 'r') as file:
                next(file)
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) < 10:
                        raise ValueError("Incorrect file format")
                    number = int(parts[0])
                    name = parts[1].strip().lower()
                    types = [parts[2].strip()]
                    if parts[3].strip():
                        types.append(parts[3].strip())
                    stats = tuple(map(int, parts[4:10]))
                    pokémon = cls(number, name, types, stats)
                    cls.__pokémon_data[name] = pokémon
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except ValueError as e:
            print(f"Error in file format: {e}")

    @classmethod
    def get_pokémon_details(cls, pokémon_input: str or int):
        """
        Retrieves details of a Pokémon by its name or Pokedex number.

        Args:
            pokémon_input (str or int): The name or Pokedex number of the Pokémon.

        Returns:
            Pokémon or None: The Pokémon instance if found, None otherwise.
        """
        pokémon_input = str(pokémon_input).strip().lower()
        if pokémon_input in cls.__pokémon_data:
            return cls.__pokémon_data[pokémon_input]
        elif pokémon_input.isdigit():
            for pokémon in cls.__pokémon_data.values():
                if pokémon.number == int(pokémon_input):
                    return pokémon
        return None
