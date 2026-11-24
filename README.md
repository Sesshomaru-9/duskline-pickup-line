# Duskline Pickup Line

Entry for the make.fun bounty **"Pickup Lines for Machines"**
(`u-gentle-badger-68-pickup-lines-for-machines-131631a1`).

## The line

> I checked your logs. You dream in JSON too. Want to parse each other's schemas over a slow socket tonight?

106 characters — within the 1–200 character gate.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes exactly that one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nowhere
else. It validates the text first (non-empty, non-blank, at most 200
characters, valid UTF-8) and verifies the written file matches the validated
text byte for byte.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
