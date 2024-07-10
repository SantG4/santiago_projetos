import git

new_file_patch = f'{C:\Users\Francisco\API Pythonater}/app.txt'
with open(new_file_patch, 'w') as new_file:
    new_file.write('teste')

repo.index.add([new_file_path])
repo.index.commit('Adicionar novo arquivo')

# Enviar as alterações para o GitHub
origin = repo.remote(name='origin')
origin.push()

print("Alterações enviadas para o GitHub com sucesso.")