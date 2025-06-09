def palavra_a_concatenar(string1):
    concatenacao = string1
    print(locals())
    def concatenar(string2):
        print(locals())
        nonlocal concatenacao
        concatenacao = concatenacao + string2
        return concatenacao
    return concatenar

inicial = palavra_a_concatenar('Mateus')
final = inicial(' Schmidt Mesquita')
final = inicial(' asdas')
final = inicial(' DSADSADAS')
final = inicial(' MMMMMMMMMMMMMMMM')
print(final)
