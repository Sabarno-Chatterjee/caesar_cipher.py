alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Enter\n").lower()
shift = int(input("Enter a shift value.\n"))
new = ""
for i in text:
    place = alphabet.index(i)
    out = place + shift
    if out < 26:
        new = new + alphabet[out]
    elif out >= 26:
        #out = shift - (shift - 1)
        out = out - place
        new = new + alphabet[out-1]

print(new)

#Working so far except shift values of why and lower when it crosses limit
