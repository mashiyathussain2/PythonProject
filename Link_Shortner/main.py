import pyshorteners

link = input("Enter your link: ")
print("Your short link is: ", pyshorteners.Shortener().tinyurl.short(link))
