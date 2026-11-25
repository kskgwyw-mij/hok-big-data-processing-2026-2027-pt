# LLM extraction batch

1. Give each line of `chunks.jsonl` to a model together with `prompt.md`.
2. Write the model's answers to `answers.jsonl`, one JSON object per line:
   `{"source_id": "...", "observations": [ ... ]}`
3. Run `python3 -m engine llm-apply exports/llm/answers.jsonl`.

Every observation is validated against `schema.json`; an evidence span that does not occur
in the source text is rejected. Accepted observations go through the same belief updater.
