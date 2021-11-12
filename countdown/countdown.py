
# import the time module
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

    def main():
        path = input("https://static.wikia.nocookie.net/pokemon-nederland/images/c/c2/Pikachu-dex.png/revision/latest?cb=20150504204448&path-prefix=nl : \n")
        try:
            image = PIL.Image.open(path)
        except:
            print(path, "Unable to find image ");
    
    #from pyfiglet import figlet_format  
    #print( figlet_format("Spooyboy2000", font = "standard" ) )
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))