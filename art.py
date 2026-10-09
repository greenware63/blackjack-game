GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

# ---- "BLACKJACK" block letters (raw strings so backslashes are safe) ----
GLYPHS = {
    "B": [r" ____  ",
          r"| __ ) ",
          r"|  _ \ ",
          r"| |_) |",
          r"|____/ "],
    "L": [r" _     ",
          r"| |    ",
          r"| |    ",
          r"| |___ ",
          r"|_____|"],
    "A": [r"    _    ",
          r"   / \   ",
          r"  / _ \  ",
          r" / ___ \ ",
          "/_/   \\_\\"],
    "C": [r"  ____ ",
          r" / ___|",
          r"| |    ",
          r"| |___ ",
          r" \____|"],
    "K": [r" _  __",
          r"| |/ /",
          r"| ' / ",
          r"| . \ ",
          "|_|\\_\\"],
    "J": [r"     _ ",
          r"    | |",
          r" _  | |",
          r"| |_| |",
          r" \___/ "],
}


def build_word(word):
    rows = [""] * 5
    for ch in word:
        g = GLYPHS[ch]
        w = max(len(line) for line in g) + 1  # +1 column gap between letters
        for i in range(5):
            rows[i] += g[i].ljust(w)
    return rows


word_rows = build_word("BLACKJACK")
INNER = max(len(r) for r in word_rows) + 2  # box inner width (keeps total under 80 cols)
word_rows = [r.center(INNER) for r in word_rows]

top = f"{GREEN}  ╔{'═' * INNER}╗{RESET}"
bottom = f"{GREEN}  ╚{'═' * INNER}╝{RESET}"
box_lines = "\n".join(
    f"{GREEN}  ║{BOLD}{YELLOW}{r}{RESET}{GREEN}║{RESET}" for r in word_rows
)

TOTAL = INNER + 4


def center(plain, colored):
    pad = max(0, (TOTAL - len(plain)) // 2)
    return " " * pad + colored


border_top = f"{CYAN}  ♠ ─── ♣ {'─' * (INNER - 18)} ♣ ─── ♠{RESET}"
border_bot = f"{CYAN}  ♥ ─── ♦ {'─' * (INNER - 18)} ♦ ─── ♥{RESET}"

tag_plain = "[♠] PAYS 3:2  •  DEALER STANDS ON 17 [♦]"
tag = center(
    tag_plain,
    f"{CYAN}[{RED}♠{CYAN}] PAYS 3:2  •  DEALER STANDS ON 17 [{RED}♦{CYAN}]{RESET}",
)

cards = [
    r"  .------. .------.",
    r"  |A .--. | |K .--. |",
    r"  | :/\: | | :/\: |",
    r"  | (__) | | :\/: |",
    r"  | '--' A| | '--' K|",
    r"  `------' `------'",
]

# Hand-made card art with suit colors
card_art = [
    f"{WHITE}   .------.   .------.{RESET}",
    f"{WHITE}   |{RED}A{WHITE}.--. |   |{RESET}{WHITE}K{WHITE}.--. |{RESET}",
    f"{WHITE}   | :{RED}/\\{WHITE}: |   | :{WHITE}(){WHITE}: |{RESET}      {YELLOW}21{RESET}",
    f"{WHITE}   | {RED}(__){WHITE} |   | {WHITE}()(){WHITE} |{RESET}   {YELLOW}♠ ♥ ♦ ♣{RESET}",
    f"{WHITE}   | '--'{RED}A{WHITE}|   | '--'{WHITE}K{WHITE}|{RESET}",
    f"{WHITE}   `------'   `------'{RESET}",
]
card_pad = " " * ((TOTAL - 24) // 2)
card_art = [card_pad + line for line in card_art]

colored_logo = "\n".join(
    [border_top, *card_art, top, box_lines, bottom, tag, border_bot]
)


