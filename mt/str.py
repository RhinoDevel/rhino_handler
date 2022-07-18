
# Marcel Timm, RhinoDevel, 2022jul18

def is_str(s):
    return isinstance(s, str)

def is_nonwhitespace(s):
    """Is given argument a string that is neither empty, nor whitespace-only?"""

    return is_str(s) and s and not s.isspace()
