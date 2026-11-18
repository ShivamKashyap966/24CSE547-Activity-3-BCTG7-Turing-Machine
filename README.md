# Inside the Universal Computing Machine

**Course:** 24CSE547 - Formal Languages and Automata Theory  
**Activity:** 3 Peer Teaching  
**Group:** 24CSE547S5 BCTG7

## Team

- Aryan (24BTRBT016)
- Shivam (24BTRBT025)
- Sudheer (24BTRBT028)

**Under the Supervision of Dr. Devaraj Verma C**  
Course Instructor, Department of CSE (Blockchain Technology), FET, JU

## Project

This project contains a single-tape Turing Machine that decides:

```text
L = {0^n1^n | n >= 0}
```

The machine marks each `0` as `X`, finds the next unmarked `1`, marks it as `Y`, and returns to the leftmost unpaired symbol. It accepts when all symbols have been paired. It rejects when it finds a mismatch or an extra symbol.

## How to Run

```bash
python tm_0n1n.py
```

No external libraries are required.

## Test Cases

| Input | Expected Result |
|---|---|
| `0011` | ACCEPTED |
| `0010` | REJECTED |
| Empty string | ACCEPTED |
| `010` | REJECTED |
| `000111` | ACCEPTED |
| `01` | ACCEPTED |

## Why the Language Is Decidable

A Turing Machine can always finish for every input in `0^n1^n`. It repeatedly removes one `0` and one `1`, or detects a mismatch. There are only finitely many symbols and the head has a systematic search and return process, so the machine cannot loop forever on valid or invalid strings.

For an input with no remaining unmarked symbols, the machine reaches `q_accept`. For any differing number of zeros and ones, an incorrect arrangement, or a symbol outside the language format, it reaches `q_reject`. Therefore, the Turing Machine always halts and correctly accepts or rejects every input.
