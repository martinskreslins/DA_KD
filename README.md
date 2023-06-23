# DA_KD
Attempt at AES 128. Developed based on NIST published paper: https://doi.org/10.6028/NIST.FIPS.197-upd1
### BEFORE YOU USE:
'AES_128.py' Works, but some parts of text can fail to decrypt properly because of encoding errors. <br>
'AES_128_custom_charmap_version.py' Hotfixed version by using a custom charmap.<br>
Key provided in input can be any length except null. If  input length is 16 key is unmodified. Else key is lenghtened or shortened it to 16 symbols.<br>
Folder names are to remain UNCHANGED.<br>
'data' folder holds data (plaintext) to encrypt. 'Latin_1' 0-255 symbols ONLY. <br>
'data to decrypt' holds 'AES_128.py' encryption results.<br>
'decrypted_data' holds 'AES_128.py' decryption results.<br>
'custom_charmap_data to decrypt' holds 'AES_128_custom_charmap_version.py' encryption results.<br>
'custom_charmap_decrypted_data' holds 'AES_128_custom_charmap_version.py' decryption results.<br>
### HOW TO USE:
1. Paste files (.txt only) to encrypt in 'data' folder.<br>
2. Run either 'AES_128_custom_charmap_version.py'(reccomended) or 'AES_128.py' (not reccomended)<br>
3. Type in your key.<br>
4. Pick your option: 'e' to encrypt, 'd' to decrypt, any other key to exit program.<br>