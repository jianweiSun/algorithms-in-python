
value_list_ = [1, 5, 10, 25]
known_table_ = {1: 1, 5: 1, 10: 1, 25: 1}


def calculate_change(amount, value_list=value_list_, known_table=known_table_):

    min_coin = None
    if amount in known_table:
        return known_table[amount]
    else:
        value_list_need_process = [v for v in value_list if v < amount]
        for v in value_list_need_process:
            new_min_coin = 1 + calculate_change(amount - v)

            if amount not in known_table or new_min_coin < known_table[amount]:
                known_table[amount] = new_min_coin

            if not min_coin or new_min_coin < min_coin:
                min_coin = new_min_coin

    return min_coin


