def solution(n, k, cmds):
    answer = ''
    size, pos = n, k
    buffer = []
    
    def parse_command(command):
        split_commands = command.split(" ")
        if split_commands[0] in ("D", "U"):
            return split_commands[0], int(split_commands[1])
        else:
            return split_commands[0], None
    
    table = [i for i in range(n)]
    
    for i, cmd in enumerate(cmds):
        c, unit = parse_command(cmd)
        if c == "U":
            pos = max([pos - unit, 0])
        elif c == "D":
            pos = min([pos + unit, size -1])
        elif c == "C":
            deleted = table.pop(pos)
            buffer.append((pos, deleted))
            size -= 1
            # print(f"delete: {deleted}\t table: {table} buffer: {buffer}\n")
        elif c == "Z":
            idx, recovered = buffer.pop()
            table.insert(idx, recovered)
            size += 1
            # print(f"recover: {recoverd} table: {table} buffer: {buffer}\n")
    
    # print(table)
    # print(buffer)
    
    j = 0
    _answer = []
    for i in range(n):
        if table[j] == i:
            _answer.append("O")
            j += 1
        else:
            _answer.append("X")
    
    answer = "".join(_answer)
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))