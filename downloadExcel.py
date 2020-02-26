import dropbox
import os

def download(dbx, folder, subfolder, name):
    """Download a file.
    Return the bytes of the file, or None if it doesn't exist.
    """
    path = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), name)
    while '//' in path:
        path = path.replace('//', '/')
    with stopwatch('download'):
        try:
            md, res = dbx.files_download(path)
        except dropbox.exceptions.HttpError as err:
            print('*** HTTP error', err)
            return None
    data = res.content
    print(len(data), 'bytes; md:', md)
    return data

def stopwatch(message):
    """Context manager to print how long a block of code took."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))

#SE GENERA EL ACCESO A DROPBOX USANDO LA CLAVE QUE GENERO DESDE MI CUENTA
dbx = dropbox.Dropbox("JK894OVzkD8AAAAAAAABql5v19mpIfSZx9k8I6cZCwkoSb7l-2tB9MAZw0hl2uVT")

try:
    dbx.users_get_current_account()
except AuthError:
    print("Token inválido, intente generar uno nuevo")

for entry in dbx.files_list_folder("").entries:
    print(entry.name)


data = download(dbx, "2020 Torneo de Clausura", "", "Control de jornadas de jugadores y clubes TC 2020 Mario")

print(data)