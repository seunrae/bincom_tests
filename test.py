def analyze_colors(colors):
	mean_color = max(set(colors), key=colors.count);
	
	color_count = {};
	for color in colors:
		color_count[color] = color_count.get(color, 0) + 1;
	most_worn_color = max(color_count, key=color_count.get);

	sorted_colors = sorted(colors);
	middle = len(sorted_colors) // 2;
	median_color = sorted_colors[middle];

	variance = sum((colors.count(color) - len(colors) / 2) ** 2 for color in set(colors)) / len(colors);

	return mean_color, most_worn_color, median_color, variance;

dress_colors = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
				"ARSH", "BROWN", "GREEN", "BROWN", 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE',
				'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE',
				'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',
				'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE'
				];

mean_color, most_worn_color, median_color, variance = analyze_colors(dress_colors);

red_probability = dress_colors.count("RED") / len(dress_colors);

print("1. Mean color of shirts: {}".format(mean_color));
print("2. Color mostly worn throughout the week: {}".format(most_worn_color));
print("3. Median color of shirts: {}".format(median_color));
print("4. Variance of colors: {}".format(variance));
print("5. Probability of choosing red at random: {:.2%}".format(red_probability));