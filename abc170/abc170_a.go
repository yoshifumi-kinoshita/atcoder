package main

import (
	"bufio"
	"fmt"
	"os"
	//"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	slice := strings.Split(s, " ")
	for i, x := range slice {
		if x == "0" {
			fmt.Println(i + 1)
			os.Exit(0)
		}
	}
}
