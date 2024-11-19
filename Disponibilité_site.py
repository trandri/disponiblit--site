import socket
import ssl

#TODO ajouter la vérification du certificat s'il est valide ou pas

hostname = "google.com"
context = ssl.create_default_context() #Créer un contexte SSL/TLS avec des paramètre par défaut

try:
     with socket.create_connection((hostname, 443), timeout=5) as sock: # Créer une conexion TCP/IP sans SSl
        with context.wrap_socket(sock, server_hostname=hostname) as ssock: # Transforme le socket en rajoutant SSL
           cert = ssock.getpeercert() # Récupère le certificat SSl
           if cert:
               print("Le site est sécurisé")
           else:
                print("Le site n'est pas sécurisé")
except Exception:
    print("Le site à mis trop de temps ou n'existe pas")
            