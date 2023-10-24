s = input('Enter the ciphertext: ')
max_letter = ''
max_count = 0
for j in range(len(s)):
    letter = s[j]
    count = 0 
    for i in range(len(s)):
        if s[i] == letter:
            count += 1
            if count > max_count:
                max_count = count
                max_letter = letter 
print(f'The most common letter is {max_letter}')

distance = ''
distance = abs(ord(max_letter) - ord('E'))

print(f'The secret key is {distance}')

real_text = ''
real_distance = 0
for n in range(len(s)):
    if 65 <= ord(s[n]) <= 90 :
        real_distance = ord(s[n]) - distance
        if real_distance < 65:
            real_distance += 26
    else:
        real_distance = ord(s[n])
    real_text += chr(real_distance)

print(real_text)

