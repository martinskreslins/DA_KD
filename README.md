# DA_KD
# Attempt at AES 128.
#
# BEFORE YOU USE:
# 'AES_128.py' Works, but some parts of text can fail to decrypt properly because of encoding errors.
# 'AES_128_custom_charmap_version.py' Hotfixed version by using a custom charmap.
# Key provided in input can be any length except null. If  input length is 16 key is unmodified. Else key is lenghtened or shortened it to 16 symbols.
# Folder names are to remain UNCHANGED.
# 'data' folder holds data (plaintext) to encrypt. 'Latin_1' 0-255 symbols ONLY. 
# 'data to decrypt' holds 'AES_128.py' encryption results.
# 'decrypted_data' holds 'AES_128.py' decryption results.
# 'custom_charmap_data to decrypt' holds 'AES_128_custom_charmap_version.py' encryption results.
# 'custom_charmap_decrypted_data' holds 'AES_128_custom_charmap_version.py' decryption results.
# HOW TO USE:
# 1. Paste files (.txt only) to encrypt in 'data' folder.
# 2. Run either 'AES_128_custom_charmap_version.py'(reccomended) or 'AES_128.py' (not reccomended)
# 3. Type in your key.
# 4. Pick your option: 'e' to encrypt, 'd' to decrypt, any other key to exit program.
