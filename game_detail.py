from random import choice

COLOR_LIST  = ["#FF6E31", "#FD8A8A", "#91D8E4", "#DC0000", "#FFF6BD", "#C0EEE4", "#F8F988", "#FF7000"]


for chosen_color in range(len(COLOR_LIST)):
    color = choice(COLOR_LIST)

    print(color)