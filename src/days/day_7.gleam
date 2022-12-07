import gleam/map
import gleam/list
import gleam/string
import gleam/int

type D =
  List(String)

type FS =
  map.Map(D, List(#(String, Int)))

fn parse(input: String) -> FS {
  let #(_, fs) =
    string.split(input, "\n")
    |> list.fold(
      #([], map.new()),
      fn(acc, line) {
        let #(current_dir, fs) = acc
        case line {
          "$ cd /" -> #([""], fs)
          "$ cd .." -> {
            let [_, ..parent] = current_dir
            #(parent, fs)
          }
          "$ cd " <> d -> #([d, ..current_dir], fs)
          "$ ls" -> acc
          sz_name -> {
            assert Ok(#(sz, name)) = string.split_once(sz_name, " ")
            assert Ok(sz) = case sz {
              "dir" -> Ok(0)
              _ -> int.parse(sz)
            }
            let path = current_dir
            let ls = case map.get(fs, path) {
              Ok(ls) -> [#(name, sz), ..ls]
              _ -> [#(name, sz)]
            }
            #(current_dir, map.insert(fs, path, ls))
          }
        }
      },
    )
  fs
}

fn totals(fs: FS, path: D) -> Int {
  // sum files and subdirectories
  assert Ok(files) = map.get(fs, path)

  files
  |> list.map(fn(f) {
    case f {
      #(name, 0) -> totals(fs, [name, ..path])
      #(_, sz) -> sz
    }
  })
  |> int.sum
}

pub fn pt_1(input: String) -> Int {
  let fs = parse(input)
  fs
  |> map.map_values(fn(key, _value) { totals(fs, key) })
  |> map.values
  |> list.filter(fn(s) { s <= 100000 })
  |> int.sum
}

pub fn pt_2(input: String) -> Int {
  let fs = parse(input)
  let fst =
    fs
    |> map.map_values(fn(key, _value) { totals(fs, key) })

  assert Ok(used) = map.get(fst, [""])

  let unused = 70000000 - used
  let required = 30000000 - unused

  assert Ok(result) =
    fst
    |> map.values
    |> list.filter(fn(s) { s > required })
    |> list.sort(int.compare)
    |> list.first

  result
}
