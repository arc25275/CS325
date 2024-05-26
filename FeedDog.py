def feedDog(hunger_level, biscuit_size):
    dog_count = 0
    biscuit_size.sort()  # Sort biscuit sizes in ascending order
    for hunger in hunger_level:
        for i, size in enumerate(biscuit_size):
            if size >= hunger:
                del biscuit_size[i]  # Remove the used biscuit from the list
                dog_count += 1
                break
    return dog_count