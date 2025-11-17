import keyword, builtins, sys

print("=== TODOS OS COMANDOS, FUNÇÕES E MÓDULOS DO PYTHON ===\n")

print("PALAVRAS RESERVADAS:")
print(", ".join(keyword.kwlist), "\n")

print("FUNÇÕES EMBUTIDAS (built-ins):")
print(", ".join([name for name in dir(builtins) if not name.startswith("__")]), "\n")

print("MÓDULOS EMBUTIDOS DISPONÍVEIS:")
print(", ".join(sys.builtin_module_names))