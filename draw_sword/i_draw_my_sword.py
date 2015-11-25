def i_draw_my_sword(hilt, blade, material):
    if hilt < 1 or blade < 1:
        return False
    else: return get_hilt(hilt) + get_blade(blade, material)

def get_hilt(length):
    hilt = "O"
    for i in range(0, length):
        hilt += "="

    return hilt + "||"

def get_blade(length, material):
    blade = ""
    for i in range(0, length):
        blade += material

    return blade + ">"