def format_name(f_name, l_name):
    """This function converts the name into Camel Case."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("SaraNg", "daGDu")

length = len(formatted_name)



