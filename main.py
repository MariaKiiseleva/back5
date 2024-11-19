if __name__ == "__main__":
    from functions import *

    # Вызов всех функций для демонстрации
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
    call_all_functions()

