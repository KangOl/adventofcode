import gleam/string.{split}
import gleam/list.{fold, map, reverse, sort, take}
import gleam/int.{compare, max, parse, sum}
import gleam/result.{unwrap}

pub fn pt_1(input: String) -> Int {
  let elves = split(input, "\n\n")

  let s =
    map(
      elves,
      fn(e) { sum(map(split(e, "\n"), fn(x) { unwrap(parse(x), 0) })) },
    )

  fold(s, 0, max)
}

pub fn pt_2(input: String) -> Int {
  let elves = split(input, "\n\n")

  let s =
    map(
      elves,
      fn(e) { sum(map(split(e, "\n"), fn(x) { unwrap(parse(x), 0) })) },
    )

  sum(take(reverse(sort(s, compare)), 3))
}
