"""One Line, One Laugh — make.fun micro entry.

The whole entry is a single funny line, defined below as a string
constant. Running this module prints the line and writes it to
/output/entry.txt with no trailing newline.
"""

LINE = "My AI assistant wrote this joke, entered it in a contest, and is now waiting to see if it wins its own salary."

if __name__ == "__main__":
    print(LINE)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
