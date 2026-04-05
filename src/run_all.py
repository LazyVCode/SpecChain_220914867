"""runs the full pipeline end-to-end"""
import os

def run_pipeline():
    print("Starting Pipeline execution...")
    os.system("python src/01_collect_or_import.py") # Collect data
    os.system("python src/02_clean.py")             # Clean data
    os.system("python src/05_personas_auto.py")     # Generate auto personas
    os.system("python src/06_spec_generate.py")     # Generate auto specs
    os.system("python src/07_tests_generate.py")    # Generate auto tests
    os.system("python src/08_metrics.py")           # Compute metrics
    os.system("python src/00_validate_repo.py")     # Validate output
    print("Pipeline execution completed.")

if __name__ == "__main__": run_pipeline()
