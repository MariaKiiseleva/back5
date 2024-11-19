# Шаг 1: Функция, принимающая список и возвращающая перевёрнутый список.
def reverse_list(input_list):
    # Реализация функции
    return input_list[::-1]

# Шаг 2: Функция, принимающая список и изменяющая его значения.
def update_list(original_list, new_values):
    # Реализация функции
    return original_list + new_values[:len(original_list)]

# Шаг 3: Функция, сравнивающая два или более списка.
def compare_lists(*lists):
    # Реализация функции
    return len(set.intersection(*map(set, lists))) == len(lists)

# Шаг 4: Функция, выбирающая диапазон из списка с заданным шагом.
def select_range_from_list(input_list, start, end, step=1):
    # Реализация функции
    return input_list[start:end:step]

# Шаг 5: Функция, создающая список на основе переданных параметров.
def create_list_from_params(length, type, increment):
    # Реализация функции
    if type.lower() == "even":
        return list(range(increment, length * increment + increment, increment))
    elif type.lower() == "odd":
        return list(range(increment, length * increment + increment, increment))
    else:
        raise ValueError("Invalid type")

# Шаг 6: Функция, вставляющая элемент в заданную позицию списка.
def insert_element_at_position(original_list, position, value):
    # Реализация функции
    return original_list[:position] + [value] + original_list[position:]

# Шаг 7: Функция, объединяющая списки и сортирующая их.
def sort_list_by_multiple_criteria(*lists):
    # Реализация функции
    combined_list = [item for sublist in lists for item in sublist]
    return sorted(combined_list)

# Шаг 8: Функция, извлекающая минимальный элемент списка.
def remove_min_element(input_list):
    # Реализация функции
    return min(input_list)

# Шаг 9: Функция, работающая с кортежами.
def tuple_operations(*tuples):
    # Реализация функции
    result = []
    for tup in tuples:
        result.append(type(tup))
    return tuple(result)

# Шаг 10: Функция, работающая с словарями.
def dictionary_operations(dict1, dict2):
    # Реализация функции
    combined_dict = {**dict1, **dict2}
    return sum(combined_dict.values())

# Шаг 11: Функция, ищущая элемент в словаре.
def search_in_nested_dictionary(nested_dict, key):
    # Реализация функции
    result = None
    for k, v in nested_dict.items():
        if isinstance(v, dict):
            result = search_in_nested_dictionary(v, key)
        elif k == key:
            return v
    return result

# Шаг 12: Функция для вызова всех других функций.
def call_all_functions():
    print("Результат работы функций:")
    print(reverse_list([3, 1, 4, 1, 5]))
    print(update_list([1, 2, 3], [10, 20, 30]))
    print(compare_lists([1, 2, 3], [1, 2, 3]))
    print(select_range_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 7))
    print(create_list_from_params(5, "even", 2))
    insert_element_at_position([1, 2, 3, 4, 5], 3, 10)
    sort_list_by_multiple_criteria(["gold", "silver", "platinum"], ["price", "weight"])
    remove_min_element([5, 2, 8, 1, 9])
    tuple_operations((1, 2, 3), (4, 5, 6))
    dictionary_operations({"a": 1, "b": 2}, {"c": 3, "d": 4})
    search_in_nested_dictionary({"key1": {"key2": {"key3": "value"}}}, "key3")

# Вызов всех функций для демонстрации
call_all_functions()