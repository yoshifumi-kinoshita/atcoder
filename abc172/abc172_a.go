package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	a, _ := strconv.Atoi(s)
	fmt.Println(a + int(math.Pow(float64(a), 2)+math.Pow(float64(a), 3)))
}
