import re 


def name_validator(name:str) -> str :
    err : str
    space_characters = re.findall(r"\s",name)
    number_in_str = bool(re.search(r"\d",name))
    valide_name = bool(re.findall(r"^[a-zA-Z]{5,20}\s[a-zA-Z]{5,20}$",name))

    if name is False or name == "  ":
        err = "Name can not be blank"
        return err

    elif len(space_characters) > 1:
        err = "Invalide Input: name must contain only a space between first and last name"
        return err
   
    elif number_in_str:
        err = "Invalide Input: name can't contain numbers"
        return err
    
    elif valide_name is False:
        err =  """
            Invalide Input: Input must contain
            first and last name only each with alphabetic
            charaters with length not less than 5 or more than 20
            characters spearated by a space.
            """
        return err

    return "Validation successful"


name = name_validator("chile64")
print(name)

