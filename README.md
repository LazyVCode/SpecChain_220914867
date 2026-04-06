# EECS4312_W26_SpecChain - Headspace Requirements Pipeline

**Application Analyzed:** Headspace
**Dataset Size:** 1,500 collected reviews, thoroughly cleaned.

### Repository Structure
- `data/` : JSON datasets and manual/auto/hybrid review groupings.
- `personas/` : User personas generated across the three pipelines.
- `spec/` : Requirements specifications in Markdown format.
- `tests/` : Validation test suites mapped to requirements.
- `metrics/` : Computed performance metrics for pipeline comparison.
- `src/` : Python execution scripts.
- `prompts/` : Saved LLM prompt configurations.
- `reflection/` : Final analytical reflection.

### Execution Instructions
1. Install dependencies: `pip install google-play-scraper pandas nltk groq`
2. Set API Key: `export GROQ_API_KEY="Add_your_api_key_here"`
3. Run the automated pipeline: `python3.11 src/run_all.py`
