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
	a := string(slice[0])
	b := string(slice[1])
	A, _ := strconv.Atoi(a)
	B, _ := strconv.Atoi(b)

	fmt.Println((A - 1) * (B - 1))
}
