class Person:
    """Person class"""
    speech = "something in English"
    def __init__(self,name):
        self.name=name

    def print_conv(self):
        print("P1:This person whose name is " + self.name +" is speaking something.")
        print("P2: But what is he speaking?")


    def answer(self):
        print("P1: The person said " + self.speech + " .That was inaudible.")

someone = Person("bob")
someone.print_conv()
someone.answer()