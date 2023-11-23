pessoa = {'nome': 'Profe Ana', 'idade': 38, 'curso':['ingles', 'portugues']}
type(pessoa)
dir(dict)
len(pessoa)

pessoa
pessoa['nome']
pessoa['idade']
pessoa['curso']
pessoa['curso'][1]
# pessoa['tags']
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade')
pessoa.get('tags')
pessoa.get('tags', [])

pessoa = {'nome': 'Prof. Alberto', 'idade': 42, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa.pop('idade')
pessoa.update({'idade': 40, 'sexo': 'm'})
pessoa
del pessoa['cursos']
pessoa
pessoa.clear()
pessoa