
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


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


