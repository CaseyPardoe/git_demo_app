def get_income_tax(salary):
    personal_allowance = 11850
    basic_rate = 34500
    higher_rate = 150000

    if salary <= personal_allowance:
        return 0
    elif salary <= basic_rate:
        return (salary - personal_allowance) *0.2
    elif salary <= higher_rate:
        basic_tax = (basic_rate - personal_allowance) * 0.2
        higher_tax = (salary - basic_rate) * 0.4
        return basic_tax + higher_tax
    else:
        basic_tax = (basic_rate - personal_allowance) * 0.2
        higher_tax = (higher_rate - basic_rate) * 0.4
        additional_tax = (salary - higher_rate) * 0.45
        return basic_tax + higher_tax + additional_tax
    
print(get_income_tax(12500))
print(get_income_tax(40500))
print(get_income_tax(170500))