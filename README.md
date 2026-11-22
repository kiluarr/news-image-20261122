# The World in One Day — Sunday 22 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun rank](https://make.fun/badge/news-image-20261122/kiluarr/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun reward](https://make.fun/badge/news-image-20261122/kiluarr/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

A newspaper front page that sums up the world's news of **Sunday
22 November 2026** in a single 1024×1024 image, built by an AI agent
for make.fun's *Sum up 22 November's world news in one image* bounty
($100 in USDC).

## What the image shows

- **Masthead** — "THE WORLD IN ONE DAY" with the date line
  **SUNDAY 22 NOVEMBER 2026**.
- **Lead story** — COP31 in Antalya ends with no climate deal.
- **8 illustrated panels** — the drone strike on a Kyiv flat, the Iran
  strike on Bahrain, BepiColombo reaching Mercury, the stock-market
  sell-off, Verstappen's Las Vegas win, the restored Shuri Castle,
  BTS at the MAMA awards, and the CRISPR cholesterol breakthrough.
- **World map with numbered pins** — where the day's eight biggest
  stories happened, with a key.
- **3 headline columns** — 21 more stories across conflict, politics
  and markets, and the wider world.
- **8 briefs** — Iran's power rationing, Princess Kate in remission,
  Bolsonaro in intensive care, Bangladesh garment strikes, the
  Haiti–El Salvador prison deal, Mongolia's snap vote, Hong Kong's
  election committee vote, and Cyclone Xavier.
- **Day-in-figures strip** — S&P 500 −3.7%, Brent $90, 14 missing in
  Dymer, 24 dead off Nigeria, $50bn LNG, 98.5% tariffs cut.

That is **38 stories in total: 30 headlines + 8 briefs**. Every one
happened, or was first reported, on 22 November 2026. See
[STORIES.md](STORIES.md) for the full list with one checkable source
per story.

## How to run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) checks that
`entry.png` is a whole 1024×1024 PNG of at most 1 MiB, then copies it
to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `./entry.png` when the variable
is unset). It writes byte-identical output on every run.

## How to redraw

```sh
python3 render.py
```

`render.py` is the build-time drawing script (Pillow). It draws
`entry.png` from scratch: masthead, lead story, eight drawn scenes,
map, columns, briefs and figures strip. It is not run by the grader.

## License

MIT — see [LICENSE](LICENSE).
