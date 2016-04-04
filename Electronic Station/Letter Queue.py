def letter_queue(commands):
    queue = []
    for i in commands:
        com = i.split(' ')
        if com[0] == 'PUSH':
            queue.append(com[1])
        else:
            if queue:
                queue.pop(0)
    return ''.join(queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
