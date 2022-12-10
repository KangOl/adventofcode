import gleam/string
import gleam/int
import gleam/list
import gleam/pair

pub fn signal(input: String) -> List(Int) {
  {
    use x, inst <- list.map_fold(string.split(input, "\n"), 1)
    case inst {
      "noop" -> #(x, [x])
      "addx " <> y -> {
        assert Ok(y) = int.parse(y)
        #(x + y, [x, x])
      }
    }
  }
  // |> io.debug
  |> pair.second
  |> list.flatten
}

pub fn pt_1(input: String) {
  input
  |> signal
  |> list.index_map(fn(i, x) { #(i + 1, x) })
  |> list.filter_map(fn(s) {
    let #(i, x) = s
    case int.modulo(i - 20, 40) {
      Ok(0) -> Ok(i * x)
      _ -> Error(Nil)
    }
  })
  |> int.sum
}

pub fn pt_2(input: String) {
  let lines =
    input
    |> signal
    |> list.index_map(fn(i, x) { #(i + 1, x) })
    |> list.sized_chunk(40)
    |> list.map(fn(row) {
      row
      |> list.map(fn(s) {
        let #(cycle, x) = s
        assert Ok(crt) = int.modulo(cycle - 1, 40)
        case x - crt {
          -1 | 0 | 1 -> "#"
          _ -> " "
        }
      })
      |> string.join("")
    })
  ["", ..lines]
  |> string.join("\n")
}
