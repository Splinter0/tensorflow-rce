# Tersorflow Remote Code Execution with Malicious Model

Repository for the scripts presented in the blogpost: 
https://splint.gitbook.io/cyberblog/security-research/tersorflow-remote-code-execution-with-malicious-model

## Files

- `exploit.py`: used to create a simple malicious model with a reverse shell
- `inject.py`: injects the malicious layer in a legitimate model
- `model.py`: simulate the usage of `load_mode` on a malicious model
- `detector.py`: detects a malicious `Lambda` in a `.h5` model

## Disclaimer

The contents of this repository are exclusively for research and entertainment purposes.