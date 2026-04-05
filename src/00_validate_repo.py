"""checks required files/folders exist"""
import os

def check_repo():
    required_files = [
        "data/reviews_clean.jsonl",
        "personas/personas_manual.json",
        "spec/spec_auto.md",
        "tests/tests_hybrid.json"
    ]
    print("Checking repository structure...")
    all_found = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"{file_path} found")
        else:
            print(f"{file_path} NOT FOUND")
            all_found = False
    
    if all_found:
        print("Repository validation complete.")
    else:
        print("Repository validation failed. Missing files.")

if __name__ == "__main__":
    check_repo()
