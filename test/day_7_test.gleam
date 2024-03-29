import gleam/string.{trim}
import gleeunit/should
import days/day_7

const input = "
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"

pub fn pt_1_test() {
  input
  |> trim
  |> day_7.pt_1
  |> should.equal(95437)
}

pub fn pt_2_test() {
  input
  |> trim
  |> day_7.pt_2
  |> should.equal(24933642)
}
