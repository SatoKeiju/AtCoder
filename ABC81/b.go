package main

import (
  "fmt"
)

func checkEven(a []int) bool {
  for i := 0; i < len(a); i++ {
    if a[i] % 2 != 0 {
      return false
    }
  }
  return true
}

func main() {

}
