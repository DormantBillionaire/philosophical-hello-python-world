def main():
      initial_greeting = input("Hello, Pyth- uhm who are you? ")

      initial_response = print("Well, hello" , initial_greeting,"I didn't expect to see you here! Welcome to the Gen-Phil-ator!")
      initial_question = input("Anywho, tell me how your day has been on a scale of 1 to 10? I'll match you to the quote to keep you high, or get you out the hell hole you're in!: ")
      rating_response = int(initial_question) 
      # I wonder if the above code could work without a type casting a string to an integer? 
      # Maybe I can find a project to do tomorrow that can test this out 

      if rating_response < 3: 
            print("That which does not kill us makes us stronger")
      if rating_response < 5:
            print(" The mind is everything, What you think you become")
      if rating_response < 7: 
            print("When you have a dream, you've got to grab it and never let it go")
      if rating_response < 11: 
            print(" The most important thing is to enjoy your life-to be happy- it's all that matters")
      if rating_response < 0: 
            print(" A negative? really, it cant have been that bad")
      elif rating_response == str: 
            print("I dont even want to know what that said, but it is illegal to my programing ears.. luckily")

if __name__ == "__main__":
      main()



      
