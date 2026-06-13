import json
from dataclasses import dataclass

@dataclass
class AIParameters:
    temperature: float
    top_p: float

class GenAI:
    def __init__(self):
        self.parameters = AIParameters(temperature=1.0, top_p=0.9)

    def generate_content(self):
        # Simulate content generation based on parameters
        return f"Generated content with temperature {self.parameters.temperature} and top_p {self.parameters.top_p}"

    def update_parameters(self, temperature, top_p):
        self.parameters = AIParameters(temperature=temperature, top_p=top_p)

    def get_parameters(self):
        return self.parameters

class UI:
    def __init__(self, genai):
        self.genai = genai

    def display_parameters(self):
        parameters = self.genai.get_parameters()
        print(f"Current parameters: temperature={parameters.temperature}, top_p={parameters.top_p}")

    def update_parameters(self, temperature, top_p):
        self.genai.update_parameters(temperature, top_p)

def main():
    genai = GenAI()
    ui = UI(genai)

    while True:
        print("1. Display parameters")
        print("2. Update parameters")
        print("3. Generate content")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            ui.display_parameters()
        elif choice == "2":
            temperature = float(input("Enter new temperature: "))
            top_p = float(input("Enter new top_p: "))
            ui.update_parameters(temperature, top_p)
        elif choice == "3":
            print(genai.generate_content())
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
