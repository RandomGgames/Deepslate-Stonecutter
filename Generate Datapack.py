import json

recipes = [
		"cobbled_deepslate",
		"polished_deepslate",
		"deepslate_bricks",
		"cracked_deepslate_bricks",
		"deepslate_tiles",
		"cracked_deepslate_bricks",
		"chiseled_deepslate",
		"cobbled_deepslate_wall",
		"polished_deepslate_wall",
		"deepslate_brick_wall",
		"deepslate_tile_wall",
		"cobbled_deepslate_stairs",
		"polished_deepslate_stairs",
		"deepslate_brick_stairs",
		"deepslate_tile_stairs",
		"cobbled_deepslate_slab",
		"polished_deepslate_slab",
		"deepslate_brick_slab",
		"deepslate_tile_slab"
	]

for recipe in recipes:
	dict = {
		"type": "minecraft:stonecutting",
		"ingredient": {
			"item": "minecraft:deepslate"
		},
		"result": f"minecraft:{recipe}",
		"count": 1
	}
	with open(f"data/minecraft/recipes/{recipe}_from_deepslate_stonecutting.json", "w") as f:
		json.dump(dict, f, indent = "\t")
