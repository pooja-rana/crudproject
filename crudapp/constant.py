from enum import Enum


class CommonConst(Enum):
    """ Only Number constant for enumeration """

    CELL_NUMBER = "^[+]?[0-9]{6,15}$"
    PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&^()_+|}" \
                     r"{\]\[:><.,\/\\;'=~`\"-])[A-Za-z\d@$!#%*?&^()_+|}{\]\[:><.,\/\\;'=~`\"-]{8,64}$"
