import os
import sys

def run_pipeline():
    # sys.executable automatically finds the exact Python version you are running
    python_exec = sys.executable 
    
    print(f"Starting Pipeline execution using: {python_exec}")
    os.system(f"{python_exec} src/01_collect_or_import.py") 
    os.system(f"{python_exec} src/02_clean.py")             
    os.system(f"{python_exec} src/05_personas_auto.py")     
    os.system(f"{python_exec} src/06_spec_generate.py")     
    os.system(f"{python_exec} src/07_tests_generate.py")    
    os.system(f"{python_exec} src/08_metrics.py")           
    os.system(f"{python_exec} src/00_validate_repo.py")     
    print("Pipeline execution completed.")

if __name__ == "__main__": 
    run_pipeline()
