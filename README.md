# examen_2
https://github.com/acasasaez/examen_2.git

El código escrito en los comits previos a este ( exceptuando el método fight_attack de la clase principal) es código hecho prácticamente todo por mí acorde a mis conocimientos. Digo prácticamente porque en la parte del constructor cuando la modifiqué le eché un vistazo a la solución para ayudarme. 
A partir de ahora no sé cómo seguir.

Para este proyecto debíamos programamar un juego de pokemons. 

Nuestro trabajocontaba con diferentes apartados. 

En la primera parte debíamos programar la clase pokemon y crear las subclases pokemon de aire, agua, tierra y electricidad ( que heredarían de la clase pokemon).

En la segunda parte debíamos modificar las subclases para que tuviesen métodos y atributos propios : 

  1. El pokemon de agua debía tener un índice de ataque entre 11 y 20 puntos.
  2. En el pokemon de aire debíamos modificar su método de defensa para que hubiese un 50 % de probabilidades de que el ataque no le afectase.
  3. El pokemon de tierra debía tener un índice de defensa entre 11 y 20 puntos.
  4. En el pokemon eléctrico debíamos modificar el método de lucha para que hubiese un 50% de probabilidad de que el daño provocado se duplicase

Hasta aquí el trabajo aportado por mí 

En la tercera parte debíamos programar el main, configurando los pokemnos deseados. 

Además, las características de cada grupo de pokemons se introducen a través de archivos csv. 

Esto, más la clase de tipo de arma no sabía programarlas. 

Código: 
MAIN: 
```
import csv
import copy

from tipo_arma import WeaponType
from pokemon import Pokemon


def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      Null .

    Example
    -------
      >>> get_data_from_user("file.csv")
    """
    set_of_pokemons = []

    if not isinstance(name_file, str):
        raise TypeError("The paramenter name_file is not a String.")

    name_file_s = name_file

    try:
        with open(name_file_s, newline='') as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)

        for temp_pokemon_csv in data_from_file:
            coach_pokemon = Pokemon(int(temp_pokemon_csv[0]),
                                    temp_pokemon_csv[1],
                                    WeaponType.from_str(temp_pokemon_csv[2]),
                                    int(temp_pokemon_csv[3]),
                                    int(temp_pokemon_csv[4]),
                                    int(temp_pokemon_csv[5]))

            set_of_pokemons.append(coach_pokemon)

    except SyntaxError:
        print("Oops! The Pokemons of the coach were not introduced correctly." +
                " Try again...")

    return set_of_pokemons


def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Null .

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """
    if isinstance(list_of_pokemons,list):

        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("All pokemons should be Pokemon Type")
        print("Please Coach " + str(coach_to_ask) + " introduce the ID of the Pokemon: " + "\n")

        while True:
            print("List of Pokemons: " + "\n")
            
            for i in list_of_pokemons:
                print(i)
            
            string_introduced = input(":~>")
            try:
                int_introduced= int(string_introduced)
            except ValueError:
                print("Please, introduce an ID present in the list:")
            for temp_pokemon in list_of_pokemons:
                if int_introduced == temp_pokemon.get_id():
                    return temp_pokemon
            print("Please, introduce a number present in the list: ")
    else:
        raise TypeError("list_pokemons should be a list")


def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Null .

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """

    if isinstance(list_of_pokemons, list):
        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("All pokemons should be pokemon Type")

    defeated = True

    for temp_pokemon in list_of_pokemons:
        if temp_pokemon.is_alive():
            defeated = False

    return not defeated


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    print("For Game User 1: \n")
    game_user_1 = get_data_from_user("coach_1_pokemons.csv")

    # Get configuration for Game User 2.
    print("For Game User 2: \n")
    game_user_2 = get_data_from_user("coach_2_pokemons.csv")

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    temp_list_pokemons_from_coach_1 = game_user_1
    list_pokemons_alive_coach_1 = copy.copy(temp_list_pokemons_from_coach_1)

    temp_list_pokemons_from_coach_2 = game_user_2
    list_pokemons_alive_coach_2 = copy.copy(temp_list_pokemons_from_coach_2)

    # Choose first pokemons
    print("Coach 1 choose your first pokemon")
    temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Please coach 1 introduce the id of the pokemon:", list_pokemons_alive_coach_1)
    print("Coach 2 choose your first pokemon")
    temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Please coach 2 introduce the id of the pokemon:",list_pokemons_alive_coach_2)

    while(coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):

        if not temp_pokemon_coach_1.is_alive():
            # Select a new pokemon
            print("Coach 1 your pokemon: " + str(temp_pokemon_coach_1) + " has been defeated. Please select the new pokemon to fight ")
            list_pokemons_alive_coach_1.remove(temp_pokemon_coach_1)
            temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Please coach 1 introduce the id of the pokemon", list_pokemons_alive_coach_1)
        if not temp_pokemon_coach_2.is_alive():
            # Select a new pokemon
            print("Coach 2 your pokemon: " + str(temp_pokemon_coach_2) + " has been defeated. Please select the new pokemon to fight ")
            list_pokemons_alive_coach_2.remove(temp_pokemon_coach_2)
            temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Please coach 2 introduce the id of the pokemon", list_pokemons_alive_coach_2)

        print("pokemon from Game User 1 attacks.")
        temp_pokemon_coach_1.fight_attack(temp_pokemon_coach_2)
        print("pokemon from Game User 2 attacks.")
        temp_pokemon_coach_2.fight_attack(temp_pokemon_coach_1)


    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")
    if (coach_is_undefeated(temp_list_pokemons_from_coach_1)and not coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("The WINNER is Game User 1.")
    elif (not coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("The WINNER is Game User 2.")
    else:
        print("Both Game Users have been defeated. There is a DRAW.")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    for temp_pokemon in temp_list_pokemons_from_coach_1:
        print(temp_pokemon)

    print("Game User 2:")
    for temp_pokemon in temp_list_pokemons_from_coach_2:
        print(temp_pokemon)


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
