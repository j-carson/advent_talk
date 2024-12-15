from watchfiles import run_process


if __name__ == "__main__":
    run_process("./solution.py", target="uv run solution.py", target_type="command")
