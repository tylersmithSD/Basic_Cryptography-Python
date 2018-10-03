#Developer: Tyler Smith
#Date:      10.19.16
#Purpose:   The program takes an english word that the user types in
#           and encrypts it, making it secret. The user also has
#           the option to take an encrypted word and decrypt it,
#           revealing its english translation. There is also an
#           additional choice the user has, randomizing
#           the encryption key.

#Import library to randomize key
import random

#The menu function greets the user asking them what they want to do
def menu():
  print('\nSecret Decoder Menu')      # Name of program
  print('0) Quit')                    # Ends program
  print('1) Encode')                  # Encode english word
  print('2) Decode')                  # Decode encrypted word
  print('3) Generate new key')        # New key

  # See what the user would like to do
  userResponse = input('What would you like to do? ')

  return userResponse                  # Return user response

#Encode function encrypts english word
def encode(encodeText):
  encodeStr  = True                   # Determines whether we should be looping or not
  encodeChar = ''                     # Character that we want to encrypt
  index      = 0                      # Position of encodeChar in alpha string
  keyChar    = ''                     # Corresponding key character for encodeChar
  loopCount  = -1                     # Keeps track of how many characters we have encrypted 
  endLoop    = ((len(encodeText)) - 1)# This ensures we know when to stop looping 
  output     = ''                     # Defines variable output

  #Begin encoding string
  while encodeStr:
    loopCount = (loopCount + 1)       # Keeps track of what character we are on in encodeText 
    encodeChar = encodeText[loopCount]# Character that we want to encode
    encodeChar = encodeChar[0].upper()# Convert character to uppercase so we can encode
    
    if(encodeChar != ' '):            # If character isn't a space, do this
     index  = alpha.index(encodeChar) # Find position where encodeChar exists in alpha string
     keyChar = key[index]             # Get corresponding encoded character
     output = (output + keyChar)      # Set the output = to what we have + the new keyChar we just found
    else:                             # If character is a space, do this
     keyChar = '_'                    # Set keyChar = underscore so representing a space
     output = (output + keyChar)      # Set the output = to what we have + the new keyChar we just found
    
    if(loopCount == endLoop):         # If we are done encoding each string, end loop
      return output                   # Return what we encoded
      encodeStr = False               # Change loop condition, so we exit loop

#Decode encoded string
def decode(decodeText):
  decodeStr  = True                   # Determines whether we should be looping or not
  decodeChar = ''                     # Character that we want to decrypt
  index      = 0                      # Position of decodeChar in key string
  alphaChar  = ''                     # Corresponding alpha character for decodeChar
  loopCount  = -1                     # Keeps track of how many characters we have encrypted 
  endLoop    = ((len(decodeText)) - 1)# This ensures we know when to stop looping
  output     = ''                     # Defines variable output
  
  while decodeStr:
    loopCount = (loopCount + 1)       # Keeps track of what character we are on in decodeText
    decodeChar = decodeText[loopCount]# Character that we want to decode
    decodeChar = decodeChar[0].upper()# Convert character to uppercase so we can decode
    
    if(decodeChar != '_'):            # If character isn't a space, do this
     index  = key.index(decodeChar)   # Find position where decodeChar exists in key string
     alphaChar = alpha[index]         # Get corresponding decoded character
     output = (output + alphaChar)    # Set the output = to what we have + the new keyChar we just found
    else:                             # If character is an underscore, do this
     alphaChar = ' '                  # Set alphaChar = to a space
     output = (output + alphaChar)    # Set the output = to what we have + the new keyChar we just found
    
    if(loopCount == endLoop):         # If we are done decoding each string, end loop
      return output                   # Return what we decoded 
      decodStr = False                # Change loop condition, so we exit loop

#Randomize key string
def randomizeKey():
  keyRandom = ''.join(random.sample(key,len(key))) #Randomize it and store it as variable
  return keyRandom                    # Return what we randomize

#Main processing of entire program  
def main():
  global alpha                          # These variables need to be defined here as global
  global key                            # so they can be changed in the program
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Enlgish key of encrypted word
  key   = "XPMGTDHLYONZBWEARKJUFSCIQV"  # Encrypted key of english word
  
  keepGoing = True                   
  while keepGoing:
    response = menu()
    if response == "1":               # User wants to encode text
      plain = input("Text to be encoded: ")
      print(encode(plain))
      
    elif response == "2":             # User wants to decode text
      coded = input("Code to be decyphered: ")
      print (decode(coded))

    elif response == "3":
      key = randomizeKey()
      
    elif response == "0":             # User wants program to end
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
      
    else:                             # User entered input wrong
      print ("I don't know what you want to do...")

#Run main function 
main()
