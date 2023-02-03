import json

recipes = {
		"cobbled_deepslate": 1,
		"polished_deepslate": 1,
		"deepslate_bricks": 1,
		"cracked_deepslate_bricks": 1,
		"deepslate_tiles": 1,
		"cracked_deepslate_bricks": 1,
		"chiseled_deepslate": 1,
		"cobbled_deepslate_wall": 1,
		"polished_deepslate_wall": 1,
		"deepslate_brick_wall": 1,
		"deepslate_tile_wall": 1,
		"cobbled_deepslate_stairs": 1,
		"polished_deepslate_stairs": 1,
		"deepslate_brick_stairs": 1,
		"deepslate_tile_stairs": 1,
		"cobbled_deepslate_slab": 2,
		"polished_deepslate_slab": 2,
		"deepslate_brick_slab": 2,
		"deepslate_tile_slab": 2
	}

for item, count in recipes.items():
	dict = {
		"type": "minecraft:stonecutting",
		"ingredient": {"item": "minecraft:deepslate"},
		"result": f"minecraft:{item}",
		"count": count
	}
	with open(f"data/minecraft/recipes/{item}_from_deepslate_stonecutting.json", "w") as f:
		json.dump(dict, f, indent = "\t")