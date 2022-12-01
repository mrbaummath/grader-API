import random
import string




def generate_section_code(all_codes,code=None, count = 0):
    if code is not None and code not in all_codes:
        return code
    if count > 20:

        return False
    else:
        count += 1
        chars = string.digits + string.ascii_uppercase
        code = random.sample(chars, 7)
        code = ''.join(code)
        return generate_section_code(all_codes,code, count)

        