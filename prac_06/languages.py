"""
CP1404 Practical - Programming Language Analyzer
Estimated: 40 minutes
Actual: 37 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Analyze programming languages for dynamic typing"""
    python = ProgrammingLanguage("Python", "Static", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Static",  True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages_list = [python, ruby, visual_basic]
    dynamically_typed_languages = []  # Create an empty list to store dynamically typed languages

    print("The dynamically typed languages are:")
    for language in languages_list:
        if language.is_dynamic():
            dynamically_typed_languages.append(language.name)
            print(language.name)

    if not dynamically_typed_languages:
        print("No dynamically typed languages found in the list.")


if __name__ == '__main__':
    main()
