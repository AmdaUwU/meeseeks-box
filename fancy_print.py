import subprocess
import os
import platform

script_dir = os.path.dirname(os.path.realpath(__file__))


def print_stream(content):
    style_file = "ressources/gpt_style.json"
    fancy_out = subprocess.run(
        [f"glow -s '{script_dir}/{style_file}' -w {terminal_width}"],
        shell=True,
        input=(content).encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    fancy_string = fancy_out.stdout.decode("utf-8")
    lines = fancy_string.split("\n")
    lines_num = len(lines)

    # Number of lines to be overiden by new print
    amount_to_print = min(terminal_height - 3, lines_num)
    global last_lines_num
    number_of_new_lines = lines_num - last_lines_num
    amount_to_erase = amount_to_print - (number_of_new_lines)

    print(f"\033[{amount_to_erase}A", end="\r")
    for line in lines[-amount_to_print:]:
        print(line)
    last_lines_num = lines_num


def init_print():
    get_terminal_dimentions()
    global last_lines_num
    last_lines_num = 0


def get_terminal_dimentions():
    global terminal_height, terminal_width
    os = platform.system()
    match os:
        case "Linux":  # Probably works on macos as well but needs testing
            out_stty = subprocess.run(
                ["stty size"], shell=True, capture_output=True
            )
            terminal_height, terminal_width = out_stty.stdout.decode().split(
                " "
            )
        case _:
            print(f"live printing on {os} is not currently supported")
    terminal_height, terminal_width = int(terminal_height), int(terminal_width)


def terminal_dims_windows(): # not tested
    import ctypes

    STD_OUTPUT_HANDLE = -11
    h = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

    if res:
        import struct

        (
            bufx,
            bufy,
            curx,
            cury,
            wattr,
            left,
            top,
            right,
            bottom,
            maxx,
            maxy,
        ) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        width = right - left + 1
        height = bottom - top + 1
        print("Terminal width:", width)
        print("Terminal height:", height)
    else:
        print("Error getting console screen buffer info")
