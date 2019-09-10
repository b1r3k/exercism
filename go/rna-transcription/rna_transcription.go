package strand

var trans = map[string]string{
	"G": "C",
	"C": "G",
	"T": "A",
	"A": "U",
}

func ToRNA(dna string) string {
	var transcript = ""
	for _, element := range dna {
		transcript += trans[string(element)]
	}
	return transcript
}
