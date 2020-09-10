def calc_total(interest_rate, starting_amount, years_save, years_til_retire, contrib_amount):
    scale = (1+interest_rate)**(years_til_retire)
    total = starting_amount*scale

    for i in range(1, years_save+1):
        scale = (1+interest_rate)**(years_til_retire - i)
        total += scale*contrib_amount

    return total

print(calc_total(.1, 52979, 0, 35, 48750))

print(calc_total(.1, 52979, 4, 35, 48750))
