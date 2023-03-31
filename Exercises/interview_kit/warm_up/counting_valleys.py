def counting_valleys(steps, path):
    height = 0
    valley_counter = 0
    for steps in path:
        if steps == 'U':
            if height == -1:
                valley_counter += 1
            height += 1
        else:
            height -= 1
    return valley_counter
