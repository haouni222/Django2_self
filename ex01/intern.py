class Intern:
    def __init__(self, string):
        if string is None or string == "":
            self.Name = "My name? I’m nobody, an intern, I have no name."
        else:
            self.Name = string
        
    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted"
    
    def work(self):
        raise Exception("I'm just an intern, i cant do that...")

    def make_coffee(self):
        return self.Coffee()

def main():
    Nobody = Intern("")
    Mark = Intern("Mark")

    print(Nobody)
    print(Mark)
    print(Mark.make_coffee())
    try :
        Nobody.work()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()