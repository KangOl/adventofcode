import gleam/string
import gleam/list
import gleeunit/should
import days/day_5

fn trim_nl(str: String) -> String {
  string.split(str, "\n")
  |> list.drop_while(fn(e) { e == "" })
  |> list.reverse
  |> list.drop_while(fn(e) { e == "" })
  |> list.reverse
  |> string.join("\n")
}

const input = "
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"

pub fn pt_1_test() {
  input
  |> trim_nl
  |> day_5.pt_1
  |> should.equal("CMZ")
}

pub fn pt_2_test() {
  input
  |> trim_nl
  |> day_5.pt_2
  |> should.equal("MCD")
}
