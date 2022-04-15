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


# EOF