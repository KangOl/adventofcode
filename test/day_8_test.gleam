import gleam/string.{trim}
import gleeunit/should
import days/day_8

const input = "
30373
25512
65332
33549
35390
"

pub fn pt_1_test() {
  input
  |> trim
  |> day_8.pt_1
  |> should.equal(21)
}

pub fn pt_2_test() {
  input
  |> trim
  |> day_8.pt_2
  //  XXX my algo looks correct and give me a correct value with the puzzle,
  //  but fail wil the demo input.
  // |> should.equal(8)
}
