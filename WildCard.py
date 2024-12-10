wild = 'ge*ks'
pattern = 'geeks'
def match(self, wild, pattern):
    for let1 in wild:
        for let2 in pattern:
            if let1 != "*" or let1 != "?":
                if wild.index(let1) == pattern.index(let2) and let1 == let2:
                    return True

match(wild, pattern)
