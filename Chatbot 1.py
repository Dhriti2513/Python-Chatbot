def chatbot(): # main function chatbot
    while True:
        user_input = input("Enter Your Choice:")
        user_input = user_input.lower().strip()  # <-- Added .strip() to remove extra spaces
        if user_input in ["hello", "hi", "hey", "good morning", "good evening"]:
            answer = ["Bot: Hey! How are you? ",
                      "Bot: Hello, How are you?",
                      "Bot: Hey Welcome to Mychatbot ",
                      "Bot: Hello Good Morning",
                      "Bot: Hello Good Evening"]
            import random
            print(random.choice(answer))

        elif user_input in ["i am feeling sad", "i am feeling depressed", "i am feeling unhappy"]:
            print("Don't worry, be happy!")
            print("Always believe in yourself.")

        # ...existing code...
        elif "what can you do ?" in user_input:
            print  ("Hey Welcome to My Chatbot\n")
            print  ("U can learn anything using wikipedia \n")
            print  ("Solve basic math problem\n")
            print  ("Read Quotes\n")
            print  ("U can create Qr\n")
            print  ("Know Current Date & time\n")
            print  ("Generate Otp\n")
            print  ("Calculate Age\n")
            print  ("Hey Welcome to My Chatbot\n")

      
     
        elif "want to learn new topic"  in user_input or "learn" in user_input:
            topic=input("What do you want to learn: ")
            import wikipedia as wp
            try:
                summary=wp.summary(topic)
                print(summary)
            except wp.DisambiguationError as e:
                print("The topic you entered is ambiguous. Please be more specific.")
                print("Possible options:", e.options)
            except wp.PageError:
                print("Sorry, no page found for your topic.")
            except Exception as ex:
                print("An error occurred:", ex)
            
        elif "solve math problem" in user_input or "solve" in user_input:

            print("You can solve any expression here \n")
            choice=input("What do you want to solve: ")
            exp=eval(input("Enter Expression: "))
            print(exp)
        
        elif "quote" in user_input or "motivate me" in user_input:
            
            quotes = ["Believe in yourself and all that you are!",
             "The harder you work, the luckier you get.",
             "Push yourself, because no one else is going to do it for you.",
             "Great things never come from comfort zones.",
             "Dream it. Wish it. Do it.",
             "Success doesn't just find you. You have to go out and get it.",
             "The key to success is to focus on goals, not obstacles.",
             "Dream bigger. Do bigger.",
             "Don't stop when you're tired. Stop when you're done.",]
            import random
            print("💡 Quote of the Day: ", random.choice(quotes))

            
        # CALCULATE AGE LOGIC IN YEAR
        elif "myage" in user_input or "calculate my age" in user_input:
            import datetime as dt
            age=int(input("Enter Your DOB in Year"))
            c_year = dt.datetime.now().year
            final=c_year-age
            print("You are",final,"years old")

       #CREATE QR CODE LOGIC
        elif "qr" in user_input or "createqr" in user_input:
            import qrcode as qr
            data=input("Enter data for QR")
            q=qr.make(data)
            q.save("qrbychatbot.png")
            print("Qr Saved Successfully")
            import os
            path_qr = os.path.abspath("qrbychatbot.png")
            print(path_qr)
        
        #Date and Time
        elif "time" in user_input or "current date & time" in user_input:
            import datetime
            now = datetime.datetime.now()
            print("Current Date and Time: ", now)

        # GENERATE OTP
        elif "otp" in user_input or"generateotp" in user_input:
            import random
            otp=random.randint(1000,9999)
            print(" Your Otp is: ",otp)
      
        
        elif "bye" in user_input or "will talk later" in user_input:
            print ("Thank You for using Mychatbot")
            break
        else:
            print ("I can't understand you, Please try again later") 
            
            
chatbot()  # calling chatbot function