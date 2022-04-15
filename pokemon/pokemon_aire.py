from pokemon.pokemon_clase import Pokemon
import random
from tipo_arma import WeaponType
class PokemonAir(Pokemon):
    def __init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating):
        super().__init__(self, id, pokemon_name, weapon_type, health_point, attack_rating,  defense_rating)
    
    def fight_defense(self,points_of_demage): 
        numero = random.randint (0,1)
        self.defense_rating = self.defense_rating + self.defense_rating*porcentaje_aumentado
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
