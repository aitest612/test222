"""나이와 성별을 파악"""

def user_age(year):
    return 2026 - year

def user_gender(num):
    if int(num[7]) % 2 == 0:
        return '여성'
    else:
        return '남성'