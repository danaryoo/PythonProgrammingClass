def get_login_name(first, last, idnumber):
  #Get the first 3 letters of the first name
  #if the name is less than 3 characters, the slice will return the entire first name
  set1 = first[0:3]
  set2 = last[0:3] #Exercise #2 cont. of Exercise #1
  set3 = idnumber[-3:]
  login_name = set1 + set2 + set3
  return login_name

#valid_pass func accepts a password as an argument and returns either T or F
#A valid passord must be at least 7 characters, one uppercase, one lowercase, one digit
def valid_password(password):
  correct_length = False #set bollean variables to false
  has_uppercase = False
  has_lowercase = False
  has_digit = False
  #begin the validation. start by testing the password length
  if len(password) >=7:
    correct_length = True
    #test each character and set the appropriate flag when a required character is found
    for ch in password:
      if ch.isupper():
        has_uppercase = True
      if ch.islower():
        has_lowercase = True
      if ch.isdigit():
        has_digit = True
        #determine whether all of the requirements are met
    if correct_length and has_uppercase and has_lowercase and has_digit:
      is_valid = True
    else:
      is_valid = False
  return is_valid