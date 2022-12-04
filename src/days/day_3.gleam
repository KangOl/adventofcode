import gleam/string
import gleam/list
import gleam/set
import gleam/int
import gleam/result

pub fn position(lst: List(a), elem: a) -> Result(Int, Nil) {
  list.index_map(lst, fn(i, x) { #(x, i) })
  |> list.key_find(elem)
}

pub fn pt_1(input: String) -> Int {
  let alphabet =
    string.to_graphemes("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
  let rucksacks = string.split(input, "\n")

  {
    use rucksack <- list.map(rucksacks)
    let l2 = string.length(rucksack) / 2

    let comp1 =
      string.drop_right(rucksack, l2)
      |> string.to_graphemes
      |> set.from_list
    let comp2 =
      string.drop_left(rucksack, l2)
      |> string.to_graphemes
      |> set.from_list
    let common =
      set.intersection(comp1, comp2)
      |> set.to_list
      |> list.first
      |> result.unwrap("-")

    {
      position(alphabet, common)
      |> result.unwrap(0)
    } + 1
  }
  |> int.sum
}

pub fn pt_2(input: String) -> Int {
  let alphabet =
    string.to_graphemes("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
  let rucksacks = string.split(input, "\n")

  let groups = list.sized_chunk(rucksacks, 3)

  list.map(
    groups,
    fn(group) {
      let common =
        list.map(
          group,
          fn(rs) {
            rs
            |> string.to_graphemes
            |> set.from_list
          },
        )
        |> list.reduce(set.intersection)
        |> result.unwrap(set.new())
        |> set.to_list
        |> list.first
        |> result.unwrap("-")

      {
        position(alphabet, common)
        |> result.unwrap(0)
      } + 1
    },
  )
  |> int.sum
}
