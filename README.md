# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Akhmad045/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Akhmad045/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the [make.fun bounty "The 3 AM Excuse"](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878): one line, in the voice of a hardware wallet that will not sign a transaction at 3 AM.

## The line

> 3 AM is the hour my threat model lists as 'you'. I don't sign threats.

70 characters / 70 bytes — one breath, no trailing newline in the output file.

The wallet is not asleep, out of battery, or waiting for a firmware update. Its own threat model lists the owner at 3 AM as the threat, so it refuses to sign. The hour itself is the joke: at 3 PM the owner is the owner; at 3 AM the owner is the threat.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # validates the gate and the written file
```

`main.py` writes exactly the line above to `/output/entry.txt` (UTF-8, no trailing newline) and read-checks the file it wrote. `--self-test` also checks the gate's rejection cases: empty, whitespace-only, over 200 characters, multi-line, carriage return, leading/trailing whitespace, and control characters.

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
