class VillainQuiz():
    
    def __init__(self):
        
        """
        Sets the counters for each villain to 0
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        self.counter_jafar = 0
        self.counter_ursula = 0
        self.counter_scar = 0
        self.counter_gaston = 0
        
        
    def villain_counter(self, villain):
        
        """
        If the answer matches a villain, the villain's counter is increased
        
        Parameters 
        ----------
        villain : string
            Villain whose counter is to be increased
            
        Returns
        -------
        Nothing
        """
        
        if villain == "jafar":
            self.counter_jafar += 1
        elif villain == "ursula":
            self.counter_ursula += 1
        elif villain == "scar":
            self.counter_scar += 1
        elif villain == "gaston":
            self.counter_gaston += 1


    def question_one(self):
        
        """
        Question one
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("What would you say is your best quality? \n"
              "A. Your stunning good looks \n" 
              "B. Your wicked sense of humor \n"
              "C. Your ambitious nature \n"
              "D. Your leadership qualities") 

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("jafar")
        elif answer == "B":
            self.villain_counter("ursula")
        elif answer == "C":
            self.villain_counter("scar")
        elif answer == "D":
            self.villain_counter("gaston")


    def question_two(self):
        
        """
        Question two
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("\n"
              "What ticks you off the most? \n"
              "A. Being left out \n"
              "B. Lack of control \n"
              "C. Rejection \n"
              "D. Not being respected")

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("ursula")
        elif answer == "B":
            self.villain_counter("jafar")
        elif answer == "C":
            self.villain_counter("gaston")
        elif answer == "D":
            self.villain_counter("scar")


    def question_three(self):

        """
        Question three
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("\n"
              "Which sin are you most guilty of? \n"
              "A. Envy \n"
              "B. Greed \n"
              "C. Pride \n"
              "D. Wrath")

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("scar")
        elif answer == "B":
            self.villain_counter("jafar")
        elif answer == "C":
            self.villain_counter("gaston")
        elif answer == "D":
            self.villain_counter("ursula")


    def question_four(self):

        """
        Question four
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("\n"
              "Every villain needs a sidekick. Take your pick. \n"        
              "A. Idiots who get the job done (or at least pretend they do) \n"
              "B. Mysterious but intelligent henchmen \n"
              "C. A pet that obeys orders \n"
              "D. A silly but loyal jokester")

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("scar")
        elif answer == "B":
            self.villain_counter("ursula")
        elif answer == "C":
            self.villain_counter("jafar")
        elif answer == "D":
            self.villain_counter("gaston")


    def question_five(self):

        """
        Question five
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("\n"
              "You finally get the chance to take over the world. How are you doing it? \n"    
              "A. Using manipulation \n"
              "B. Using magic \n"
              "C. Straight up fighting your enemies \n"
              "D. Getting others to do it for you")

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("jafar")
        elif answer == "B":
            self.villain_counter("ursula")
        elif answer == "C":
            self.villain_counter("gaston")
        elif answer == "D":
            self.villain_counter("scar")


    def question_six(self):
   
        """
        Question six
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("\n"
              "Let's say you finally get the upper hand over your worst enemy."
              "How would you go about punishing them? \n"           
              "A. Kill them \n"
              "B. Send a mob after them \n"
              "C. Force them to serve you \n"
              "D. Curse them or the people they love")

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("scar")
        elif answer == "B":
            self.villain_counter("gaston")
        elif answer == "C":
            self.villain_counter("jafar")
        elif answer == "D":
            self.villain_counter("ursula")


    def question_seven(self):

        """
        Question seven
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("\n"
              "You get a wish from the Genie. What are you wishing for? \n"    
              "A. Ultimate Cosmic Power \n"
              "B. To marry your true love \n"
              "C. Revenge on your enemies \n"
              "D. Control over your homeland")

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("jafar")
        elif answer == "B":
            self.villain_counter("gaston")
        elif answer == "C":
            self.villain_counter("ursula")
        elif answer == "D":
            self.villain_counter("scar")



    def question_eight(self):

        """
        Question eight
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        """
        
        print("\n"
              "Which villainous song resonates the most with you? \n"
              "A. Be Prepared \n"
              "B. Prince Ali (Reprise) \n"
              "C. Poor Unfortunate Souls \n"
              "D. Gaston")

        answer = input("Your choice: ")

        if answer == "A":
            self.villain_counter("scar")
        elif answer == "B":
            self.villain_counter("jafar")
        elif answer == "C":
            self.villain_counter("ursula")
        elif answer == "D":
            self.villain_counter("gaston")


    def result(self):

        """
        Gives the result of the quiz.

        Uses code from:
        https://stackoverflow.com/questions/3090175/python-find-the-greatest-number-in-a-list-of-numbers    

        Parameters
        ----------
        None

        Returns
        -------
        The result of the quiz
        """

        self.highestCount = max(self.counter_jafar, self.counter_ursula, self.counter_scar, self.counter_gaston)

        if self.highestCount == self.counter_jafar:
            self.villain = "jafar"
        elif self.highestCount == self.counter_ursula:
            self.villain = "ursula"
        elif self.highestCount == self.counter_scar:
            self.villain = "scar"
        elif self.highestCount == self.counter_gaston:
            self.villain = "gaston"

        print("\n"
              "You are " + self.villain + "!")

        if self.villain is "jafar":
            print("Like Jafar, you're power-hungry and you definitely don't work well under someone. \n"
                  "But you're pretty ambitious, I'll give you that. \n"
                  "My advice: Be careful what you wish for. \n")
            
        elif self.villain is "ursula":
            print("Like Ursula, you hold a grudge, and while you may seem harmless at first, \n"
                  "to others, vengefulness lurks within. \n"
                  "My advice: Don't underestimate your enemies. \n")
            
        elif self.villain is "scar":
            print("Like Scar, you've got the wits, but aren't the best at taking \n"
                  "matters into your own hands to ensure success. \n"
                  "My advice: Don't take on more than you are capable of. \n")
            
        elif self.villain is "gaston":
            print("Like Gaston, you've got some narcissistic tendencies that feed \n"
                  "into your sense of entitlement. Confident's important, but let's not take it too far. \n"
                  "My advice: Check yourself. \n")
          