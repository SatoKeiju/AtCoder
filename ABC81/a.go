package main

import  (
  "fmt"
  "strings"
)

func main() {
  var grid string
  fmt.Scan(&grid)
  fmt.Println(strings.Count(grid, "1"))
}
