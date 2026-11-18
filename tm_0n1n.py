"""
Beginner-friendly Turing Machine simulator for L = {0^n 1^n | n >= 0}.
"""


BLANK = "_"


def run_tm(input_string):
    """Run the Turing Machine, print a trace, and return its result."""
    tape = list(input_string) if input_string else [BLANK]
    head = 0
    state = "q0"
    steps = 0

    print("\nInput:", repr(input_string))

    while state not in ("q_accept", "q_reject"):
        if head < 0:
            tape.insert(0, BLANK)
            head = 0
        elif head >= len(tape):
            tape.append(BLANK)

        symbol = tape[head]
        tape_view = "".join(tape)
        print(
            f"Step {steps:3}: state={state:<8} head={head:<3} "
            f"tape={tape_view}"
        )

        if state == "q0":
            if symbol == "0":
                tape[head] = "X"
                head += 1
                state = "q1"
            elif symbol in ("X", "Y"):
                head += 1
            elif symbol == BLANK:
                state = "q_accept"
            else:
                state = "q_reject"

        elif state == "q1":
            if symbol in ("0", "Y", "X"):
                head += 1
            elif symbol == "1":
                tape[head] = "Y"
                head -= 1
                state = "q2"
            else:
                state = "q_reject"

        elif state == "q2":
            if symbol in ("0", "1", "Y"):
                head -= 1
            elif symbol == "X":
                head += 1
                state = "q0"
            else:
                state = "q_reject"

        steps += 1

    tape_view = "".join(tape).strip(BLANK)
    print(
        f"Step {steps:3}: state={state:<8} head={head:<3} "
        f"tape={tape_view if tape_view else BLANK}"
    )
    print(f"Total steps: {steps}")
    print("Final tape:", tape_view if tape_view else BLANK)
    print("ACCEPTED" if state == "q_accept" else "REJECTED")

    return "ACCEPTED" if state == "q_accept" else "REJECTED"


if __name__ == "__main__":
    test_cases = ["0011", "0010", "", "010", "000111", "01"]

    print("Turing Machine for L = {0^n1^n | n >= 0}")
    for test in test_cases:
        run_tm(test)
