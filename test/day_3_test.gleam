import gleam/string.{trim}
import gleeunit/should
import days/day_3

const input = "
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"

pub fn pt_1_test() {
  input
  |> trim
  |> day_3.pt_1
  |> should.equal(157)
}

pub fn pt_2_test() {
  input
  |> trim
  |> day_3.pt_2
  |> should.equal(70)
}
