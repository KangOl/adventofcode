import gleam/string
import gleam/int
import gleam/list
import gleam/set

fn parse(input: String) -> List(#(String, Int)) {
  input
  |> string.split("\n")
  |> list.map(fn(line) {
    assert Ok(#(w, c)) = string.split_once(line, " ")
    assert Ok(c) = int.parse(c)
    #(w, c)
  })
}

fn expand(moves: List(#(String, Int))) -> List(String) {
  moves
  |> list.map(fn(move) {
    let #(w, c) = move
    list.repeat(w, c)
  })
  |> list.flatten
}

fn sign(a: Int) -> Int {
  case a {
    0 -> 0
    _ if a > 0 -> 1
    _ -> -1
  }
}

fn follow(knot: #(Int, Int), head: #(Int, Int)) -> #(Int, Int) {
  let tail = knot
  case head.0 - tail.0, head.1 - tail.1 {
    0, 0 | 0, 1 | 0, -1 | 1, 0 | -1, 0 | 1, 1 | 1, -1 | -1, -1 | -1, 1 -> tail
    dx, dy -> #(tail.0 + sign(dx), tail.1 + sign(dy))
  }
}

fn move(head: #(Int, Int), movement: String) -> #(Int, Int) {
  case movement {
    "U" -> #(head.0, head.1 + 1)
    "D" -> #(head.0, head.1 - 1)
    "L" -> #(head.0 - 1, head.1)
    "R" -> #(head.0 + 1, head.1)
  }
}

pub fn pt_1(input: String) {
  run(input, 2)
}

pub fn pt_2(input: String) {
  run(input, 10)
}

fn run(input: String, rope_length: Int) -> Int {
  let moves =
    input
    |> parse
    |> expand

  let rope = list.repeat(#(0, 0), rope_length)

  let positions =
    moves
    |> list.scan(
      rope,
      fn(rope, movement) {
        let [head, ..tails] = rope

        let head = move(head, movement)

        let #(_, tails) =
          tails
          |> list.map_fold(
            head,
            fn(prev, knot) {
              let tail = follow(knot, prev)
              #(tail, tail)
            },
          )
        [head, ..tails]
      },
    )

  positions
  |> list.map(list.last)
  |> set.from_list
  |> set.size
}
