def create_substitution_dict(table):
    # Membuat kamus substitusi dari tabel 5x2
    substitution_dict = {}
    for i in range(len(table[0])):
        substitution_dict[table[0][i]] = table[1][i]
    return substitution_dict

def substitute_message(message, substitution_dict):
    # Substitusi pesan menggunakan kamus substitusi
    encrypted_message = ""
    for char in message:
        if char in substitution_dict:
            encrypted_message += substitution_dict[char]
        else:
            encrypted_message += char  # Jika karakter tidak ada dalam tabel, biarkan apa adanya
    return encrypted_message

# Input tabel 5x2
table = [
    ['A', 'B', 'C', 'E', 'F'],  # Baris 1 (Huruf asli)
    ['J', 'X', 'D', 'I', 'K']   # Baris 2 (Huruf pengganti)
]

# Membuat kamus substitusi dari tabel
substitution_dict = create_substitution_dict(table)

# Pesan input yang akan dienkripsi
message = "SELAMAT PAGI TEMAN-TEMAN"

# Proses substitusi (enkripsi)
encrypted_message = substitute_message(message, substitution_dict)

# Output hasil
print("Pesan asli:", message)
print("Pesan terenkripsi:", encrypted_message)
