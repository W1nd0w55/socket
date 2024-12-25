sql_output = tuple()

def username():
    try:
        # get the username from SQL output
        name = str(sql_output[1])
        return name
    except TypeError: pass
    except IndexError: pass

def admin():
    try:
        role = str(sql_output[5])
        #Q: are you admin?
        if role == 'admin': is_admin = 1
        #A: you're not
        else: is_admin = 0
        return bool(is_admin)
    except TypeError: pass
    except IndexError: pass
