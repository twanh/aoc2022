package main

import (
  "strings"
  "strconv"
  "fmt"
  "os"
  "io/ioutil"
)

func solution(s string) int {

  lines := strings.Split(s, "\n")

  curSum := 0
  maxSum := 0

  for _, line := range lines {
    if len(line) == 0 {
      if curSum >= maxSum {
        maxSum = curSum
      }
      curSum = 0
    } else {
      val, err := strconv.Atoi(line)
      if err != nil {
        fmt.Println("Could not convert str to  int....")
        continue
      }
      curSum += val
    }
  }

  return maxSum
}


func main() {

  inputFile := os.Args[1]


  file, err := ioutil.ReadFile(inputFile)

  if err != nil {
    fmt.Println("ERROR: could not read file!", err)
  }

  content := string(file)

  result := solution(content)

  fmt.Println(result)

}
