import re
import math
from datetime import datetime

# 1. Funkcja sprawdzająca poprawność adresu e-mail 
# na podstawie restrykcyjnego wzorca regex.
def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))


# 2. Funkcja obliczająca pole koła na podstawie podanego promienia.
def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Promień nie może być ujemny.")
    return math.pi * radius ** 2


# 3. Funkcja filtrująca liczby parzyste z listy wejściowej.
def filter_even(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]


# 4. Funkcja konwertująca format dat z DD-MM-RRRR na RRRR/MM/DD.
def convert_date_format(date_str: str) -> str:
    date = datetime.strptime(date_str, "%d-%m-%Y")
    return date.strftime("%Y/%m/%d")

# 5. Funkcja sprawdzająca, czy tekst jest palindromem
# ignorująca wielkość liter i znaki niealfanumeryczne.
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
