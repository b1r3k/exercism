package space

type Planet string

func Age(seconds float64, planet Planet) float64 {
	orbitalPeriods := make(map[Planet]float64)
	orbitalPeriods["Earth"] = 31557600
	orbitalPeriods["Mercury"] = orbitalPeriods["Earth"] * 0.2408467
	orbitalPeriods["Venus"] = orbitalPeriods["Earth"] * 0.61519726
	orbitalPeriods["Mars"] = orbitalPeriods["Earth"] * 1.8808158
	orbitalPeriods["Jupiter"] = orbitalPeriods["Earth"] * 11.862615
	orbitalPeriods["Saturn"] = orbitalPeriods["Earth"] * 29.447498
	orbitalPeriods["Uranus"] = orbitalPeriods["Earth"] * 84.016846
	orbitalPeriods["Neptune"] = orbitalPeriods["Earth"] * 164.79132

	return seconds / orbitalPeriods[planet]
}
