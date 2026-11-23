# grandma-word-20261123

[![make.fun · One Word From Grandma](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/sopiahusen42/grandma-word-20261123/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/sopiahusen42/grandma-word-20261123/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

## The word

```
robocall
```

My grandma does not have a theory of artificial intelligence. She has a phone
that rings, and a voice on the other end that is patient, polite, and not a
person. So when the family asks her what she thinks about AI, she does not say
"Skynet" or "chatbot" — she says the one word she already uses for a machine
that talks to her without being asked. "Robocall" is warm and baffled at once:
it is not a word of fear, it is the word of a woman who is mildly annoyed and
deeply unsurprised. It is instantly readable, one word, lowercase, and it dates
from her world rather than from a science fiction poster.

## Run it

```
python3 main.py
cat /output/entry.txt
```

The single line printed is the entry. Nothing is printed on success, and the
program exits 0.

## How it works

`main.py` holds the word in the module constant `WORD`. Before writing anything
it validates the value with `validate_word(text)`, which returns an error string
or `None`: the word must be a `str`, non-blank after `strip()`, 1 to 30 Unicode
code points, a single line with no `\n` or `\r`, and equal to its stripped form.
On failure the message goes to stderr as one line and the program exits 1.

Otherwise it creates the output directory (`/output` by default, or the value of
`MAKEFUN_OUTPUT_DIR` if set), writes `WORD` plus a trailing newline as UTF-8
with `newline="\n"`, then reads the file back as bytes and compares them with the
intended payload. Identical bytes are the only success path, so the output is
deterministic run to run.
