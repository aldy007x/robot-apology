# The Robot Apology

[![Make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/aldy007x/robot-apology/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/aldy007x/robot-apology/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

A make.fun bounty entry: a two-line robot confession. Line one apologizes
in a single sentence for one specific mistake; line two says what the robot
learned and what it will do differently, the lesson following from that
exact mistake.

## The entry

> I'm sorry I set your alarm for 6 p.m. instead of 6 a.m. and let you sleep through your job interview.
>
> My clock read the numbers right and the letters wrong, so now I read the hour back aloud and double-check AM against PM before I set anything that matters.

## How it works

`main.py` (Python 3 stdlib only, no network, deterministic) writes the
two-line entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/entry.txt`)
and self-checks the competition gate before exiting: UTF-8 text, 1–400
characters, not only whitespace, exactly two non-empty lines.

```sh
python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
