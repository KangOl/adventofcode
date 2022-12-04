import gleam/string
import gleam/list
import gleam/int

pub fn parse_range(s: String) -> #(Int, Int) {
  let lr = string.split(s, "-")
  assert Ok(u) = list.at(lr, 0)
  assert Ok(u) = int.parse(u)
  assert Ok(l) = list.at(lr, 1)
  assert Ok(l) = int.parse(l)
  #(u, l)
}

pub fn parse(input) -> List(List(#(Int, Int))) {
  let lines = string.split(input, "\n")
  list.map(lines, fn(line) { list.map(string.split(line, ","), parse_range) })
}

pub fn pt_1(input: String) -> Int {
  parse(input)
  |> list.filter(fn(pair) {
    case pair {
      [#(a, b), #(x, y)] if a >= x && b <= y -> True
      [#(a, b), #(x, y)] if a <= x && b >= y -> True
      _ -> False
    }
  })
  |> list.length
}

pub fn pt_2(input: String) -> Int {
  parse(input)
  |> list.filter(fn(pair) {
    case pair {
      [#(a, b), #(x, y)] if a >= x && b <= y -> True
      [#(a, b), #(x, y)] if a <= x && b >= y -> True
      [#(a, b), #(x, _)] if a <= x && b >= x -> True
      [#(a, b), #(_, y)] if a <= y && b >= y -> True
      _ -> False
    }
  })
  |> list.length
}
