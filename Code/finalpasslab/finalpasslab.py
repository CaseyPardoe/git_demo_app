import re

class Password_strength_checker:
    def __init__(self):
            self.password_history = {}
            
    def check_password_strength(self, password):
        if self.is_common_password(password):
            return "Very Weak"
        
        length = self.check_length(password)
        case = self.check_case(password)
        number = self.check_number(password)
        special = self.check_special(password)
    
        strength_factors = [length, case, number, special]
    
        strong_pass = True
        for factor in strength_factors:
            if factor != "Strong":
                strong_pass = False
                break
    
        if strong_pass:
            return "Very Strong"
    
        if "Moderate" in strength_factors:
            return "Moderate"
    
        if "Weak" in strength_factors:
            return "Weak"
    
        if "Very Weak" in strength_factors:
            return "Very Weak"
    
    def is_common_password(self, password):
            common_passwords = ["password","123456","qwerty", "abc123", "admin", "letmein", "welcome", "password1", "12345", "123456789"]
            return password.lower() in common_passwords
    
    def check_length(self, password):
            if len(password) >= 8:
                return "Strong"
            if 6<= len(password) < 8:
                return "Moderate"
            return "Weak"
    
    def check_case(self, password):
            if any('a' <= char <= 'z' for char in password) and any('A' <= char <= 'Z' for char in password):
                return "Strong"
            if any('a' <= char <= 'z' for char in password) or any('A' <= char <= 'Z' for char in password):
                return "Moderate"
            return "Weak"
    
    def check_number(self, password):
            if any('0' <= char <= '9' for char in password):
                return "Strong"
            return "Weak"
    
    def check_special(self, password):
            has_special_char = bool(re.search('[!@#$%^&*(),.?":{}|<>]', password))
            return "Strong" if has_special_char else "Weak"

def main():
    check_password = Password_strength_checker()
    
    while True:
        entry = input("Please enter a password to check or enter q to quit ")
        
        if entry.lower() == "q":
            break
        pass_strength = check_password.check_password_strength(entry)
        print(f"Password strength is {pass_strength}")
        
if __name__ == "__main__":
    main()
         
        
        
    
    
