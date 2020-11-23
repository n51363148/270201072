email = input("Enter an email adress:")

email = email.lower()

before_at = email.split("@")[0] #ceng113@
after_at = email.split("@")[1 ] #@example.com
before_at = before_at.replace(".","")
email = before_at + "@" + after_at

if email == "ceng113@example.com":
  print("Yes, email is ceng113@example.com")

else:
  print("No, email is not ceng113@example.com")
