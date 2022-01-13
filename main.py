alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_amonut=len(alphabet)

def cipher(message, number, task):
  cipher_txt=''
  if task=='decode':
    number*=-1
  for i in message:
    if not i in alphabet:
      cipher_txt+=i
    else:
      location=alphabet.index(i)+number
      if location>letters_amonut:
        location=location%letters_amonut
      cipher_txt+=alphabet[location]
  print(cipher_txt)



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

cipher(text, shift, direction)