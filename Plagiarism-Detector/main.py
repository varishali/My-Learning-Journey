import os
import re
from difflib import SequenceMatcher
from colorama import Fore, Style, init

init(autoreset=True)

def clean_code(code_text):
    """Code se comments aur extra spaces hatata hai normalization ke liye"""
    # Remove single line comments (# ...)
    code_text = re.sub(r'#.*', '', code_text)
    # Remove docstrings / multi-line comments
    code_text = re.sub(r'\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\"', '', code_text)
    # Remove extra whitespaces
    lines = [line.strip() for line in code_text.splitlines() if line.strip()]
    return "\n".join(lines)

def calculate_similarity(text1, text2):
    """Dono codes ke beech matching percentage calculate karta hai"""
    cleaned1 = clean_code(text1)
    cleaned2 = clean_code(text2)
    
    # SequenceMatcher algorithm
    matcher = SequenceMatcher(None, cleaned1, cleaned2)
    return round(matcher.ratio() * 100, 2)

def check_plagiarism_in_folder(folder_path):
    
    print(Fore.RED + "\n" + "="*70)
    print(Fore.CYAN + "              SMART AUTOMATED ASSIGNMENT PLAGIARISM CHECKER                ")
    print(Fore.RED + "="*70 + "\n")
    

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' nahi mila! Folder path check karein.")
        return

    # Folder se saari .py aur .txt files get karna
    files = [f for f in os.listdir(folder_path) if f.endswith('.py') or f.endswith('.txt')]
    
    if len(files) < 2:
        print("Comparison ke liye kam se kam 2 files (.py ya .txt) honi chahiye!")
        return

    print(Fore.YELLOW + "-" * 70)
    print(f"Total Assignments Found: {len(files)} files")
    print("Comparing all student submissions...\n")
    print(Fore.YELLOW + "-" * 70)
    print(f"{'Student File 1':<20} | {'Student File 2':<20} | {'Match %':<10} | {'Status'}")
    print(Fore.YELLOW + "-" * 70)

    # All Pairs Comparison
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1_path = os.path.join(folder_path, files[i])
            file2_path = os.path.join(folder_path, files[j])

            with open(file1_path, 'r', encoding='utf-8', errors='ignore') as f1, \
                 open(file2_path, 'r', encoding='utf-8', errors='ignore') as f2:
                
                content1 = f1.read()
                content2 = f2.read()

            match_score = calculate_similarity(content1, content2)

            # Plagiarism status based on score
            if match_score == 100:
                status = "EXACT MATCH (100%)"
            elif match_score >= 75:
                status = "HIGH PLAGIARISM"
            elif match_score >= 50:
                status = "MODERATE MATCH"
            elif match_score >= 25:
                status = "LOW MATCH"        
            else:
                status = "SAFE / UNIQUE"

            print(f"{files[i]:<20} | {files[j]:<20} | {match_score:>6}%   | {status}")

    print(Fore.YELLOW + "-" * 70)
    print(Fore.BLUE + "Plagiarism Check Complete!\n")

if __name__ == "__main__":
    # Assignments folder ka path
    target_folder = input("Assignments Folder Path enter karein (e.g. submissions): ").strip()
    check_plagiarism_in_folder(target_folder)