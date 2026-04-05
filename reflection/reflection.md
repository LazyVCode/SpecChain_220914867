# Pipeline Reflection

- **Most important difference:** The manual pipeline created highly constrained, specific personas rooted in actual app failures (e.g., Headspace offline audio dropping). The automated pipeline generated broader, somewhat generic personas (e.g., "The Stressed Student") that lacked technical boundary constraints.
- **Most useful pipeline:** The Hybrid pipeline. It allowed us to leverage the LLM to parse thousands of reviews for themes instantly, while human intervention was used to rewrite ambiguous acceptance criteria into testable metrics. 
- **Strongest traceability:** The manual pipeline maintained perfect 1:1 traceability because human reasoning directly linked the pain point in the review to the functional requirement. The automated pipeline occasionally "hallucinated" traceability links to review IDs that did not match the context.
- **Observed problems in automated outputs:** High Ambiguity Ratio. The LLM frequently used words like "seamlessly" or "easily" in the requirements and expected results, which cannot be programmatically validated in software testing.
