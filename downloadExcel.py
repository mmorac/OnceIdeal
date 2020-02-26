import dropbox

#SE GENERA EL ACCESO A DROPBOX USANDO LA CLAVE QUE GENERO DESDE MI CUENTA
dbx = dropbox.Dropbox("JK894OVzkD8AAAAAAAABql5v19mpIfSZx9k8I6cZCwkoSb7l-2tB9MAZw0hl2uVT")

try:
    dbx.users_get_current_account()
except AuthError:
    print("Token inválido, intente generar uno nuevo")

for entry in dbx.files_list_folder("").entries:
    print(entry.name)

