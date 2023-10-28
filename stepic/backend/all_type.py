import builtins as b

print(*[x for x in b.__dict__.values() if isinstance(x, type)], sep="\n")