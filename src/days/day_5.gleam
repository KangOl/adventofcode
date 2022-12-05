import gleam/string
import gleam/list
import gleam/regex
import gleam/option.{Some}
import gleam/int
import gleam/function.{identity}
import gleam/io

fn parse_crates(input: String) -> List(String) {
  let [numbers, ..crates] = list.reverse(string.split(input, "\n"))

  let stacks =
    numbers
    |> string.split(" ")
    |> list.filter(fn(s) { s != "" })
    |> list.length
    |> list.repeat("", _)

  list.fold(
    crates,
    stacks,
    fn(stacks, line) {
      line
      |> string.to_graphemes
      |> list.sized_chunk(4)
      |> list.map(fn(l) {
        assert Ok(a) = list.at(l, 1)
        a
      })
      |> list.zip(stacks, _)
      |> list.map(fn(t) {
        let #(a, b) = t
        string.trim(string.concat([a, b]))
      })
    },
  )
}

fn parse_moves(input: String) -> List(#(Int, Int, Int)) {
  assert Ok(re) = regex.from_string("move (\\d+) from (\\d+) to (\\d+)")
  string.split(input, "\n")
  |> list.map(fn(l) {
    assert Ok(tpl) =
      regex.scan(re, l)
      |> list.map(fn(m) {
        case m.submatches {
          [Some(m), Some(f), Some(t)] -> {
            assert Ok(m) = int.parse(m)
            assert Ok(f) = int.parse(f)
            assert Ok(t) = int.parse(t)
            #(m, f, t)
          }
        }
      })
      |> list.first
    tpl
  })
}

fn apply(
  crates: List(String),
  moves: List(#(Int, Int, Int)),
  operation: fn(List(String)) -> List(String),
) -> List(String) {
  list.fold(
    moves,
    crates,
    fn(crates, move) {
      let #(m, f, t) = move
      assert Ok(sf) = list.at(crates, f - 1)
      assert Ok(st) = list.at(crates, t - 1)

      let #(sf0, tm) =
        list.split(string.to_graphemes(sf), string.length(sf) - m)
      let st = string.concat([st, ..operation(tm)])

      list.index_map(
        crates,
        fn(i, crate) {
          case i + 1 {
            j if j == f -> string.concat(sf0)
            j if j == t -> st
            _ -> crate
          }
        },
      )
    },
  )
}

fn process(input: String, operation: fn(List(String)) -> List(String)) -> String {
  let [crates, moves] = string.split(input, "\n\n")
  parse_crates(crates)
  |> apply(parse_moves(moves), operation)
  |> list.map(fn(s) { string.slice(s, -1, 1) })
  |> string.join("")
  |> io.debug
}

pub fn pt_1(input: String) -> String {
  process(input, list.reverse)
}

pub fn pt_2(input: String) -> String {
  process(input, identity)
}
