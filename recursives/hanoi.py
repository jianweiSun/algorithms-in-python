
def move_tower(height, from_pole, middle_pole, to_pole):
    if height >= 1:
        move_tower(height-1, from_pole, to_pole, middle_pole)
        print "move disk from {} to {}".format(from_pole, to_pole)
        move_tower(height-1, middle_pole, from_pole, to_pole)
