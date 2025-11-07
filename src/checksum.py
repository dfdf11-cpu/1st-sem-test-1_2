def modulo11Checksum(ISBNNumber: str):
    digits = []
    for char in ISBNNumber:
        if char.isdigit():
            digits.append(int(char))
        elif char.upper() == 'X' and len(digits) == 9:
            digits.append(10)
    
    if len(digits) != 10:
        raise ValueError("ISBN number must contain exactly 10 digits")
    
    checkDigit = digits[-1]
    
    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight
    
    checksum = total
    return checksum % 11 == checkDigit
