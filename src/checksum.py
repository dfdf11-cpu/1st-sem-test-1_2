def modulo11Checksum(ISBNNumber: str):
    if not ISBNNumber:
        raise ValueError("ISBN number cannot be empty")
    
    digits = []
    for i, char in enumerate(ISBNNumber):
        if char.isdigit():
            digits.append(int(char))
        elif char.upper() == 'X':
            remaining_chars = ISBNNumber[i:].replace('-', '').replace(' ', '')
            if len(remaining_chars) == 1 and len(digits) == 9:
                digits.append(10)
            else:
                raise ValueError("X can only be used as the last check digit")
        elif char in ['-', ' ']:
            continue
        else:
            raise ValueError(f"Invalid character '{char}' in ISBN number")
    
    if len(digits) != 10:
        raise ValueError("ISBN number must contain exactly 10 digits")
    
    checkDigit = digits[-1]
    
    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight
    
    calculated_checksum = total % 11
    return calculated_checksum == checkDigit
