import gleam/list
import gleam/string
import gleam/set

fn run(input: String, window: Int) -> Int {
  assert Ok(#(p, _)) =
    input
    |> string.to_graphemes
    |> list.window(window)
    |> list.index_map(fn(i, x) { #(i, set.from_list(x)) })
    |> list.drop_while(fn(e) {
      let #(_, g) = e
      case set.size(g) {
        s if s != window -> True
        _ -> False
      }
    })
    |> list.first
  p + window
}

pub fn pt_1(input: String) -> Int {
  run(input, 4)
}

pub fn pt_2(input: String) -> Int {
  run(input, 14)
}
