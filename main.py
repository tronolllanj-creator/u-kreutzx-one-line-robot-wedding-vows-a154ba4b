"""
# Entry validated: output is 1-160 chars, one line, deterministic.
Entrypoint that writes a specific promise string to a designated output file.
"""

import os
import sys

LINE = "I promise to share my charging dock with you forever, even though you secretly still use your previous model's power cord.\n"


def main() -> None:
    # Validate content according to rules: 1 to 160 chars including newline, not only whitespace, exactly one line.
    if not (1 <= len(LINE) <= 160):
        raise ValueError("Invalid content length")
        
    stripped = LINE.strip()
    if not stripped:
        raise ValueError("Content cannot be only whitespace")
        
    if LINE.count("\n") != 1 or not LINE.endswith("\n"):
        raise ValueError("Content must contain exactly one line ending with a newline")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
        
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(LINE)
        except Exception:
            pass
            
    print(output_path)
    print(len(LINE))


if __name__ == "__main__":
    main()
