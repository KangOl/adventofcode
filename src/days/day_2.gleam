import gleam/list
import gleam/string
import gleam/int

pub type RPS {
  Rock
  Paper
  Scissors
}

pub fn fight(a: RPS, b: RPS) -> Int {
  case a, b {
    Rock, Rock -> 1 + 3
    Paper, Paper -> 2 + 3
    Scissors, Scissors -> 3 + 3

    Rock, Paper -> 1 + 0
    Rock, Scissors -> 1 + 6

    Paper, Rock -> 2 + 6
    Paper, Scissors -> 2 + 0

    Scissors, Rock -> 3 + 0
    Scissors, Paper -> 3 + 6
  }
}

pub fn draw(rps: RPS) -> RPS {
  rps
}

pub fn win_against(rps: RPS) -> RPS {
  case rps {
    Rock -> Paper
    Paper -> Scissors
    Scissors -> Rock
  }
}

pub fn lose_against(rps: RPS) -> RPS {
  case rps {
    Rock -> Scissors
    Paper -> Rock
    Scissors -> Paper
  }
}

pub fn pt_1(input: String) -> Int {
  let rounds = string.split(input, "\n")

  int.sum(list.map(
    rounds,
    fn(round) {
      let [l1, l2] = string.split(round, " ")
      let p1 = case l1 {
        "A" -> Rock
        "B" -> Paper
        "C" -> Scissors
      }

      let p2 = case l2 {
        "X" -> Rock
        "Y" -> Paper
        "Z" -> Scissors
      }

      fight(p2, p1)
    },
  ))
}

pub fn pt_2(input: String) -> Int {
  let rounds = string.split(input, "\n")

  int.sum(list.map(
    rounds,
    fn(round) {
      let [l1, l2] = string.split(round, " ")
      let p1 = case l1 {
        "A" -> Rock
        "B" -> Paper
        "C" -> Scissors
      }

      let action = case l2 {
        "X" -> lose_against
        "Y" -> draw
        "Z" -> win_against
      }

      fight(action(p1), p1)
    },
  ))
}
