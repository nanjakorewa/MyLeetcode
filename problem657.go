func judgeCircle(moves string) bool {
    var mc = map[string]int{"R":0, "L":0, "U":0, "D":0}
    for _, m := range moves {
        mc[string(m)] = mc[string(m)] + 1
    }

    return mc["R"]==mc["L"] && mc["U"]==mc["D"]
}