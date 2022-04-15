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

# MAIN: 
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
```

Clase Pokemon: 

```

from tipo_arma import WeaponType
class Pokemon():

    def __init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating):
        self.id = id 
        if isinstance(pokemon_name, str):
            self._pokemon_name = pokemon_name
        else:
            raise TypeError("pokemon_name es un parámetro tipo Str.")

        if isinstance(weapon_type, WeaponType):
            self._weapon_type = weapon_type
        else:
            raise TypeError("weapon_type es un parámetro tipo WeaponType.")

        if isinstance(health_point, int):
            if 1 <= health_point <= 100:
                self._health_points = health_point
            else:
                raise ValueError(" health_point debeser superir a  0 y menor o igual a 100.")
        else:
            raise TypeError("health_point debe ser un parámetro tipo Int.")

        if isinstance(attack_rating, int):
            if 1 <= attack_rating <= 10:
                self._attack_rating = attack_rating
            else:
                raise ValueError(" attack_rating debeser superior a 0 e inferior o igual a 10.")
        else:
            raise TypeError("attack_rating es un parámetro tipo Int.")

        if isinstance(defense_rating, int):
            if 1 <= defense_rating <= 10:
                self._defense_rating = defense_rating
            else:
                raise ValueError(" defense_rating debe ser superior 0 y menor o igual a  10.")
        else:
            raise TypeError(" defense_rating es un parámtro tipo Int.")
    def show(self): 
        print ("El nombre del pokemon es: ", self.pokemon_name)
        print("El id del pokemon es:", self.id)
        print("El tipo de arma del pokemon es: ", self.weapon_type)
        print("Los puntos de salud del pokemon son: ", self.health_point)
        print( "La puntuación de ataque es: ", self.attack_rating)
        print("Los puntos de defensa son: ", self.defense_rating)
    def get_id (self):
        return self.id
    def set_id (self,id):
        self.id = id

    def get_name(self):
        return self.pokemon_name
    def set_name(self, pokemon_name):
        if isinstance(pokemon_name, str):
            self._pokemon_name = pokemon_name
        else:
            raise TypeError("pokemon_name es un parámetro tipo Str.")

    def get_weapon_type(self):
        return self.weapon_type
    def set_weapon_type(self, weapon_type):
        if isinstance(weapon_type, WeaponType):
            self._weapon_type = weapon_type
        else:
            raise TypeError("weapon_type es un parámetro tipo WeaponType.")

    def get_health_point (self):
        return self.health_point
    def set_health_point(self, health_point):
        if isinstance(health_point, int):
            if 1 <= health_point <= 100:
                self._health_points = health_point
            else:
                raise ValueError(" health_point debeser superir a  0 y menor o igual a 100.")
        else:
            raise TypeError("health_point debe ser un parámetro tipo Int.")
    def get_attack_rating(self):
        return self.attack_rating
    def set_attack_rating(self, attack_rating):
        if isinstance(attack_rating, int):
            if 1 <= attack_rating <= 10:
                self._attack_rating = attack_rating
            else:
                raise ValueError(" attack_rating debeser superior a 0 e inferior o igual a 10.")
        else:
            raise TypeError("attack_rating es un parámetro tipo Int.")

    def get_defense_rating(self):
        return self.defense_rating
    def set_defense_rating(self, defense_rating):
        if isinstance(defense_rating, int):
            if 1 <= defense_rating <= 10:
                self._defense_rating = defense_rating
            else:
                raise ValueError(" defense_rating debe ser superior 0 y menor o igual a  10.")
        else:
            raise TypeError(" defense_rating es un parámtro tipo Int.")
    
    
    def is_alive (self):
        if self.health_point > 0:
            return True 
        else: 
            return False

    def   fight_attack (self, pokemon_to_attack):

        points_of_damage = self._attack_rating

        print("The Pokemon " + self._pokemon_name +
              " hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +
              " with " + str(points_of_damage) + " points of damage!")

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit
 
        

    def fight_defense(self,points_of_demage): 
  
        if self.defense_rating > points_of_demage:
            return False
        else:
            self.point_of_demage = points_of_demage - self.defense_rating
            self.health_point = self.health_point - self.point_of_demage
            print( "Puntos de salud: ", self.health_point)
            return True

   
#Repetir con todos los parámetros del constructor 
#Guardar en archivo .csv  que nos lo guardará en una tabla tipo excel 




def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


```

# Clase Pokemon de Agua:
```
from pokemon.pokemon_clase import Pokemon


from tipo_arma import WeaponType
class PokemonWater(Pokemon):
    def __init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating):
        super().__init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating)
        if isinstance(attack_rating, int):
                if 11 <= attack_rating <= 20:
                    self._attack_rating = attack_rating
                else:
                    raise ValueError(" attack_rating debeser superior o igual a 11 e inferior o igual a 20.")
        else:
                raise TypeError("attack_rating es un parámetro tipo Int.")
        
    def set_attack_rating(self, attack_rating):
        if isinstance(attack_rating, int):
            if 11 <= attack_rating <= 20:
                self._attack_rating = attack_rating
            else:
                raise ValueError(" attack_rating debeser superior o igual a 11  e inferior o igual a 20.")
        else:
            raise TypeError("attack_rating es un parámetro tipo Int.")
def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonWater(1, "Squirtle", WeaponType.HEADBUTT, 100, 12, 8)

    if pokemon_1.get_pokemon_name() == "Squirtle":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 12:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 8:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonWater(7, "Squirtle", WeaponType.HEADBUTT, 100,15, 7)

    if str(pokemon_2) == "Pokemon ID 7 with name Squirtle has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonWater(3, "Squirtle", WeaponType.KICK, 97, 15, 8)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonWater(4, "Squirtle", WeaponType.ELBOW, 93, 11, 9)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 32:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonWater(5, "Squirtle", WeaponType.PUNCH, 99, 20, 10)
    pokemon_6 = PokemonWater(6, "Squirtle", WeaponType.PUNCH, 99, 18, 9)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 88:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```

# Clase Pokemon de Aire: 
```
from pokemon.pokemon_clase import Pokemon
import random
from tipo_arma import WeaponType
class PokemonAir(Pokemon):
    def __init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating):
        super().__init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating)
    
    def fight_defense(self,points_of_demage): 
        numero = random.randint (0,1)
        if self.defense_rating > points_of_demage or numero == 1:
            return False
        else:
            self.point_of_demage = points_of_demage - self.defense_rating
            self.health_point = self.health_point - self.point_of_demage
            print( "Puntos de salud: ", self.health_point)
            return True

def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonAir(1, "Pidgey", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_pokemon_name() == "Pidgey":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonAir(7, "Pidgey", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pidgey has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonAir(3, "Pidgey", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
            
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonAir(4, "Pidgey", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_health_points() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_health_points() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonAir(5, "Pidgey", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonAir(6, "Pidgey", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 95:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```

# Clase del Pokemon Eléctrico: 
```
from tipo_arma import WeaponType
from pokemon.pokemon_clase import Pokemon
import random

class PokemonElectricity(Pokemon):
    def __init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating):
        super().__init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating)
 
    def   fight_attack (self, pokemon_to_attack):
        numero = random.randint(0,1)
        if numero == 0:
            points_of_damage = self._attack_rating
        if numero ==1:
            points_of_damage = self._attack_rating*2  
        print("The Pokemon " + self._pokemon_name +
              " hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +
              " with " + str(points_of_damage) + " points of damage!")

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit

def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonElectricity(1, "Pikachu", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_pokemon_name() == "Pikachu":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonElectricity(7, "Pikachu", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pikachu has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonElectricity(3, "Pikachu", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonElectricity(4, "Pikachu", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_health_points() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_health_points() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonElectricity(5, "Pikachu", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonElectricity(6, "Pikachu", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if (pokemon_6.get_health_points() == 95) or (pokemon_6.get_health_points() == 85):
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```
# Clase Pokemon de Tierra: 
```
from pokemon.pokemon_clase import Pokemon

from tipo_arma import WeaponType

class PokemonEarth(Pokemon):
    def __init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating):
        super().__init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating)
        if isinstance(defense_rating, int):
            if 11 <= defense_rating <= 20:
                self._defense_rating = defense_rating
            else:
                raise ValueError(" defense_rating debe ser superior o igual a 11 y menor o igual a  20.")
        else:
            raise TypeError(" defense_rating es un parámtro tipo Int.")
    def set_defense_rating(self, defense_rating):
        if isinstance(defense_rating, int):
            if 11 <= defense_rating <= 20:
                self._defense_rating = defense_rating
            else:
                raise ValueError(" defense_rating debe ser superior o igual a 11 y menor o igual a  20.")
        else:
            raise TypeError(" defense_rating es un parámtro tipo Int.")

def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonEarth(1, "Diglett", WeaponType.HEADBUTT, 100, 8, 15)

    if pokemon_1.get_pokemon_name() == "Diglett":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 15:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", WeaponType.HEADBUTT, 100, 7, 12)

    if str(pokemon_2) == "Pokemon ID 7 with name Diglett has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", WeaponType.KICK, 97, 8, 15)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonEarth(4, "Diglett", WeaponType.ELBOW, 93, 9, 11)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 34:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", WeaponType.PUNCH, 99, 10, 20)
    pokemon_6 = PokemonEarth(6, "Diglett", WeaponType.PUNCH, 99, 9, 18)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



#Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()

```



# Clase Tipo de Arma: 
```
from enum import Enum


class WeaponType(Enum):
    """Python class to implement an enumeration for the attribute Weapon Type.

    This Python class implements an enumeration for the attribute Weapon Type.

    Syntax
    ------
      obj = WeaponType.Enum

    Parameters
    ----------

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class WeaponType.

    Attributes
    ----------

    Example
    -------
      >>> from weapon_type import WeaponType
      >>> obj_WeaponType = WeaponType.Boxer
    """
    PUNCH = 2
    KICK = 4
    ELBOW = 6
    HEADBUTT = 10

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(str_weapon_type):
        """Method to obtain a Enum from a String.

        This method is used to generate a Enum based on a String.

        Syntax
        ------
          [ ] = from_str(str_weapon_type)

        Parameters
        ----------
          str_weapon_type String String that represents a Weapon Type.

        Returns
        -------
          Null .

        Example
        -------
          >>> weapon_type.from_str("punch")
        """
        str_weapon_type = str_weapon_type.lower()
        if str_weapon_type == 'punch':
            return WeaponType.PUNCH
        elif str_weapon_type == 'kick':
            return WeaponType.KICK
        elif str_weapon_type == 'elbow':
            return WeaponType.ELBOW
        elif str_weapon_type == 'headbutt':
            return WeaponType.HEADBUTT
        else:
            raise TypeError("The str " + str_weapon_type + " does not correspond with a warrior Type")


def main():
    """Function main of the module.

    The function main of this module is used to test the Class WeaponType.

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

    print("=================================================================.")
    print("Test Case 1: Check Class WeaponType - Name.")
    print("=================================================================.")

    if isinstance(WeaponType.PUNCH, WeaponType):
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.KICK, WeaponType):
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.ELBOW, WeaponType):
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.HEADBUTT, WeaponType):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class WeaponType - Value.")
    print("=================================================================.")

    if WeaponType.PUNCH.value == 2:
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.KICK.value == 4:
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.ELBOW.value == 6:
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.HEADBUTT.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


 #Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


```


# ARCHIVOS CSV 

  # Archivo 1:
  
    ```
    11,Pikachu,headbutt,69,8,8
    12,Pidgey,kick,85,7,7
    13,Squirtle,elbow,74,7,6
    ```
    
   # Archivo 2: 
   
   ```
    24,Diglett,punch,82,9,7
    25,Venusaur,kick,78,8,6
    26,Charmeleon,elbow,88,9,7
    ```
