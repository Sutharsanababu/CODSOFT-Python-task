import random
import string

class PasswordGenerator:
    def __init__(self):
        self.uppercase_letters = string.ascii_uppercase
        self.lowercase_letters = string.ascii_lowercase
        self.digits = string.digits
        self.special_characters = string.punctuation
        self.similar_characters = {'1', 'l', '0', 'O', 'I', '|'}
        self.characters = ""

    def set_options(self, include_uppercase, include_lowercase, include_digits, include_specials, exclude_similar):
        self.characters = ""
        
        if include_uppercase:
            self.characters += self.uppercase_letters
        if include_lowercase:
            self.characters += self.lowercase_letters
        if include_digits:
            self.characters += self.digits
        if include_specials:
            self.characters += self.special_characters

        if exclude_similar:
            self.characters = ''.join([c for c in self.characters if c not in self.similar_characters])

    def generate_password(self, length=12):
        if len(self.characters) == 0:
            raise ValueError("No character sets selected for password generation.")
        
        password = [random.choice(self.characters) for _ in range(length)]
        
        # Ensure at least one character from each selected category
        if length >= 4:
            if self.uppercase_letters in self.characters:
                password[random.randint(0, length - 1)] = random.choice(self.uppercase_letters)
            if self.lowercase_letters in self.characters:
                password[random.randint(0, length - 1)] = random.choice(self.lowercase_letters)
            if self.digits in self.characters:
                password[random.randint(0, length - 1)] = random.choice(self.digits)
            if self.special_characters in self.characters:
                password[random.randint(0, length - 1)] = random.choice(self.special_characters)
        
        random.shuffle(password)
        return ''.join(password)

    def run(self):
        while True:
            try:
                length = int(input("Enter the desired password length (default is 12): ") or 12)
            except ValueError:
                print("Please enter a valid number.")
                continue

            include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
            include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
            include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
            include_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'
            exclude_similar = input("Exclude similar characters (1, l, 0, O, I)? (y/n): ").strip().lower() == 'y'
            
            self.set_options(include_uppercase, include_lowercase, include_digits, include_specials, exclude_similar)
            
            try:
                password = self.generate_password(length)
                print(f"Generated Password: {password}\n")
            except ValueError as e:
                print(e)

            cont = input("Generate another password? (y/n): ").strip().lower()
            if cont != 'y':
                break

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.run()
