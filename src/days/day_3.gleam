import gleam/string
import gleam/list
import gleam/set
import gleam/int

pub fn position(lst: List(a), elem: a) -> Result(Int, Nil) {
  list.index_map(lst, fn(i, x) { #(x, i) })
  |> list.key_find(elem)
}

pub fn to_set(str: String) -> set.Set(String) {
  str
  |> string.to_graphemes
  |> set.from_list
}

pub fn first(s: set.Set(a)) -> a {
  assert Ok(f) =
    s
    |> set.to_list
    |> list.first
  f
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
      |> to_set
    let comp2 =
      string.drop_left(rucksack, l2)
      |> to_set

    let common = first(set.intersection(comp1, comp2))
    assert Ok(pos) = position(alphabet, common)
    pos + 1
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
      assert Ok(commons) =
        list.map(group, to_set)
        |> list.reduce(set.intersection)

      assert Ok(pos) = position(alphabet, first(commons))
      pos + 1
    },
  )
  |> int.sum
}
