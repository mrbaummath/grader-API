import random
import string
from .models.section_code import SectionCode

codes = SectionCode.objects.values_list('code')

def generate_section_code(code=None, count = 0):
    
    if code is not None and code not in codes:
        return code
    if count > 20:
        return False
    else:
        count += 1
        chars = string.digits + string.ascii_uppercase
        code = random.sample(chars, 7)
        generate_section_code(code, count)

        