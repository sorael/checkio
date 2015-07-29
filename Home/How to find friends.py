def check_connection(network, first, second):
    future = []
    visited = [first]
    for i in network:
        if first in i:
            future = i.split("-")

    future = set(future)
    visited = set(visited)
    future = future - visited
    future = list(future)
    visited = list(visited)
    visited += future

    while future != []:
        size = len(future)
        i = 0
        while i < size:
            for j in network:
                if future[i] in j:
                    future += j.split("-")
            i += 1
        future = set(future)
        visited = set(visited)
        future = future - visited
        future = list(future)
        visited = list(visited)
        visited += future

    flag = 0
    for i in visited:
        if i == second:
            flag += 1
        else:
            flag += 0

    if flag == 1:
        return True
    else:
        return False

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
