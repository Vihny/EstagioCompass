def funcao(*args, **kwargs):
    for arg in args:
        print(arg)
        
    for key, value in kwargs.items():
        print(f"{key} = {value}")


funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
