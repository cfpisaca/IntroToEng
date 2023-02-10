# seems simple...
# given key and dictionary, return True if key is in dictionary.keys() more than once, else False
def key_in_dict_more_than_once(key: str, d1: dict) -> bool:
    keys = []
    for i in d1.keys():
        if i == key:
            keys.append(key)
    if len(keys) > 1:
        return True
    else:
        return False


# given val and dictionary, return True if val is in dictionary.values() more than once, else False
def val_in_dict_more_than_once(d1: dict, val: int) -> bool:
    values = []
    for i in d1.values():
        if i == val:
            values.append(val)
    if len(values) > 1:
        return True
    else:
        return False


# fetch value from dictionary, return 0 if key not in dict
def fetch(k1: str, d1: dict) -> str:
    if k1 in d1.keys():
        return d1[k1]
    else:
        return 0


# given list of keys, fetch list of values from dictionary
def fetch_list(keys: list, d1: dict) -> list:
    vals = []
    for i in keys:
        if i in d1.keys():
            vals.append(d1[i])
    vals.sort()  # why do i have to sort?
    return vals


# given list of keys and list of vals, add all keys in list of keys
def add_list(keys: list, vals: list, d1: dict) -> None:
    for i in range(len(keys)):
        d1[keys[i]] = vals[i]


# given list of keys and list of vals, update all existing keys in list of keys
def overwrite(keys: list, vals: list, d1: dict) -> None:
    for i in range(len(keys)):
        if keys[i] in d1:
            d1[keys[i]] = vals[i]


# given list of keys and list of vals, add all new keys in list of keys
def add_new_keys(keys: list, vals: list, d1: dict) -> None:
    for i in range(len(keys)):
        if keys[i] not in d1:
            d1[keys[i]] = vals[i]


# given key prefix, fetch all values for matching keys
def vals_for_keys_matching(prefix: str, d1: dict) -> list:
    nlist = []
    for i in d1:
        if i.startswith(prefix):
            nlist.append(d1[i])
    return nlist


# update all items: val to [val]
def move_vals_to_list(d1: dict) -> None:
    keys = []
    vals = []
    for i in d1.keys():
        keys.append(i)
    for i in d1.values():
        vals.append(i)
    for i in range(len(keys)):
        d1[keys[i]] = [vals[i]]


# update items which don't have list values: val to [val]
def move_nonlist_vals_to_list(d1: dict) -> None:
    keys = []
    vals = []
    for i in d1.keys():
        keys.append(i)
    for i in d1.values():
        vals.append(i)
    for i in range(len(d1)):
        if type(vals[i]) == int:
            d1[keys[i]] = [vals[i]]


# two ways to remove an item from dict:
# 1. del adict["key"]
# 2. adict.pop("key")


def remove_item(key: str, d1: dict) -> None:
    if key in d1:
        d1.pop(key)


def remove_first_item(val: int, d1: dict) -> None:
    for i in d1.items():
        if val in i:
            d1.pop(i[0])
            break


def remove_all_items(val: int, d1: dict) -> None:
    remove = []
    for i in d1.keys():
        if d1[i] == val:
            remove.append([i, d1[i]])
    for i in remove:
        d1.pop(i[0])


def remove_n_items(val: int, d1: dict, n: int) -> None:
    remove = []
    count = 1
    if n != 0:
        for i in d1.keys():
            if d1[i] == val and count <= n:
                count = count + 1
                remove.append([i, d1[i]])
        for i in remove:
            d1.pop(i[0])
