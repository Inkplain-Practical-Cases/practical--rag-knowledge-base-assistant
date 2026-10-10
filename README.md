# RAG Knowledge Base Assistant

Build a runnable RAG Knowledge Base Assistant as six cumulative Python/FastAPI learning branches. Each branch isolates door, handler, service and provider modules, carries its own real tests and CRD, and supports deterministic offline reproducibility without paid inference keys.

An Inkplain practical case: a real project built step by step.

## How this repository works

Every step of the lesson has its own branch, and each one contains all steps up to it:

```bash
git clone https://github.com/Inkplain-Practical-Cases/practical--rag-knowledge-base-assistant.git
cd practical--rag-knowledge-base-assistant
git branch -r            # list the step branches
git checkout step-01-…   # code after step 1
```

`main` holds the final, complete version.
