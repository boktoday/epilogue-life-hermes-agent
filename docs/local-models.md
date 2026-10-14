# Local models: run everything offline and free

Epilogue Life touches the most personal documents a person will ever write. Running it on
local models keeps every word on the machine.

## Find what your computer can actually run

- **canirun.ai** - checks your hardware and suggests models that will run well. Start here.
- **localllm-advisor.com** and **localllm.run** - runner-ups with similar advice.

## A simple four-tier shortlist for agent work

| Tier | Model (Ollama name) | Pulls off |
|---|---|---|
| Everyday | `qwen3:8b` | warm conversation, question-asking, notes |
| Comfortable | `qwen3:14b` | better writing: reflections, letters |
| Strong | `gpt-oss:20b` | long plans, careful editing |
| Big machine | `llama3.3:70b` | near-frontier drafting |

## Setup (either one)

- **Ollama**: install, then `ollama pull qwen3:8b`. Point Hermes at `http://localhost:11434/v1`.
- **LM Studio**: install, download a model, start the server; base URL `http://localhost:1234/v1`.

Set the model and base_url in your Hermes config (see the example `config.yaml`). The
scheduled check-ins are the best place to start locally: small, frequent, private.
