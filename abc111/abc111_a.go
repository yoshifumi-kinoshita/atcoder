package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	slice := strings.Split(s, " ")
	x := string(slice[0])
	y := string(slice[1])
	X, _ := strconv.Atoi(x)
	Y, _ := strconv.Atoi(y)

	fmt.Println(X + Y/2)

}
