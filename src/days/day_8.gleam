import gleam/int
import gleam/string
import gleam/list
import gleam/set

type Tree {
  Tree(x: Int, y: Int, value: Int)
}

type Grid =
  List(List(Tree))

fn parse(input: String) -> Grid {
  input
  |> string.split("\n")
  |> list.index_map(fn(y, line) {
    line
    |> string.to_graphemes
    |> list.index_map(fn(x, v) {
      assert Ok(i) = int.parse(v)
      Tree(x, y, i)
    })
  })
}

fn fold_transform(
  lst: List(a),
  acc: b,
  transform: fn(List(a)) -> List(a),
  callback: fn(List(a), b, a, Int) -> b,
) -> b {
  let transformed = transform(lst)
  let callback0 = fn(a, b, c) { callback(lst, a, b, c) }
  let callback1 = fn(a, b, c) { callback(transformed, a, b, c) }

  list.index_fold(transformed, list.index_fold(lst, acc, callback0), callback1)
}

pub fn pt_1(input: String) {
  let grid = parse(input)

  fold_transform(
    grid,
    set.new(),
    list.transpose,
    fn(_, acc, row, _) {
      fold_transform(
        row,
        acc,
        list.reverse,
        fn(row, acc, tree: Tree, index) {
          let tree_val = tree.value
          let prevs = list.take(row, index)

          let m =
            prevs
            |> list.map(fn(t) { t.value })
            |> list.reduce(int.max)
          case m {
            Ok(v) if v >= tree_val -> acc
            _ -> set.insert(acc, tree)
          }
        },
      )
    },
  )
  |> set.size
}

fn view(
  grid: Grid,
  tree: Tree,
) -> #(List(Tree), List(Tree), List(Tree), List(Tree)) {
  assert Ok(row) = list.at(grid, tree.y)
  let on_left = list.reverse(list.take(row, tree.x))
  let [_, ..on_right] = list.drop_while(row, fn(e) { e != tree })

  let gridt = list.transpose(grid)
  assert Ok(column) = list.at(gridt, tree.x)
  let on_top = list.reverse(list.take(column, tree.y))
  let [_, ..on_bottom] = list.drop_while(column, fn(e) { e != tree })

  #(on_top, on_right, on_bottom, on_left)
}

fn distance(tree: Tree, against: List(Tree)) -> Int {
  let tree_val = tree.value

  let #(see, nosee) =
    against
    |> list.split_while(fn(e) { e.value < tree.value })

  list.length(see) + case nosee {
    [Tree(_, _, h), ..] if h == tree_val -> 1
    _ -> 0
  }
}

pub fn pt_2(input: String) {
  let grid = parse(input)

  grid
  |> list.map(fn(row) {
    row
    |> list.map(fn(tree) {
      let #(on_top, on_right, on_bottom, on_left) = view(grid, tree)

      distance(tree, on_top) * distance(tree, on_right) * distance(
        tree,
        on_bottom,
      ) * distance(tree, on_left)
    })
  })
  |> list.flatten
  |> list.fold(0, int.max)
}
