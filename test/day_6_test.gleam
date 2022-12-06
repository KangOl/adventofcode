import gleam/list
import gleeunit/should
import days/day_6

const input = [
  #("mjqjpqmgbljsphdztnvjfqwrcgsmlb", #(7, 19)),
  #("bvwbjplbgvbhsrlpgdmjqwftvncz", #(5, 23)),
  #("nppdvjthqldpwncqszvftbrmjlhg", #(6, 23)),
  #("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", #(10, 29)),
  #("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", #(11, 26)),
]

pub fn pt_1_test() {
  use test <- list.each(input)
  let #(signal, results) = test
  let #(pt1, pt2) = results

  signal
  |> day_6.pt_1
  |> should.equal(pt1)
  signal
  |> day_6.pt_2
  |> should.equal(pt2)
}
