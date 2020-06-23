package main

import (
	"bufio"
	"fmt"
	//"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	slice := strings.Split(s, " ")
	n := string(slice[0])
	k := string(slice[1])
	N, _ := strconv.Atoi(n)
	K, _ := strconv.Atoi(k)

	if N%K == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(1)
	}
}
