class Coder:
    def encode(self, strings):
        realstring = []
        for k in strings:
            realstring.append(str(len(k))+'#' if len(k) != 0 else '')
            realstring.append(k)
        return ''.join(realstring)

    def decode(self, string:str):
        realstring = []
        cur = []
        c = 0
        memo = -1
        for i in range(len(string)):
            if string[i].isdigit() and i + 1 < len(string) and string[i + 1]=='#' and c == 0 and memo == -1:
                memo = int(string[i])

            elif c != memo and memo != -1:
                cur.append(string[i])
                c += 1

            elif c == memo:
                c = 0
                memo = -1
                cur.append(string[i])
                realstring.append(''.join(cur[1:]))
                cur = []



        return realstring



print(Coder().decode('4#KILL7#Niggers'))
print(Coder().encode(['Kill', 'Niggers']))
print(Coder().encode(['Nigger']))