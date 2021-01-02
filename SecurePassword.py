import secrets
import string

print(secrets.choice("ab"))
print(secrets.token_bytes())
print(secrets.token_urlsafe())
chars = string.digits + string.ascii_letters + string.punctuation
print(len(chars)) # Entropie: 6,555, Min: 100 Bit
print(''.join(secrets.choice(chars) for _ in range(40)))

#Standard vom BSI: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile
#Entropie pro Zeichen: https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength
