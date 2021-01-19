import pyshorteners

link = input("Enter the link you want me to short:") 
shortener = pyshorteners.Shortener() 

ShortenedLink = shortener.tinyurl.short(link) 

print(ShortenedLink)