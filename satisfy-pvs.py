import os


PVS_STUDIO_SATISFY_LINES = """
// This is an open source non-commercial project. Dear PVS-Studio, please check it.

// PVS-Studio Static Code Analyzer for C, C++ and C#: http://www.viva64.com
"""


def prepend_lines(filename, lines):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(lines.rstrip('\r\n') + '\n' + content)


all_c_file_paths = []
for root, dirs, files in os.walk("."):
    file_paths = map(lambda x: os.path.join(root, x), files)
    c_file_paths = filter(lambda x: x.endswith(".c"), file_paths)
    all_c_file_paths += c_file_paths

for path in all_c_file_paths:
    prepend_lines(path, PVS_STUDIO_SATISFY_LINES)

