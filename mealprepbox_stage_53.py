# === Stage 53: Add command help text and usage examples ===
# Project: MealPrepBox
HELP = """MealPrepBox - Meal Prep Planner

Usage:
  mealprepbox.py <command> [options]

Commands:
  init              Create a fresh MealPrepBox project
  batch add <name>  Add a new batch with name and servings
  batch list        List all batches with servings
  batch remove <name>  Remove a batch by name
  container add     Add a container with meal and quantity
  container list    List all containers
  freezer add <name>  Add an item to the freezer with days left
  freezer list      List all freezer items
  freezer check     Show freezer items that are expiring soon
  reheat <name>     Print reheating notes for a batch
  help              Show this help message
  demo              Run a quick demo with sample data
  clear             Remove all data from the project

Examples:
  python mealprepbox.py init
  python mealprepbox.py batch add "Chicken Bowl" --servings 6
  python mealprepbox.py batch list
  python mealprepbox.py container add "Chicken Bowl" --count 4
  python mealprepbox.py freezer add "Soup" --days 3
  python mealprepbox.py freezer check
  python mealprepbox.py reheat "Chicken Bowl"
  python mealprepbox.py demo
"""


def print_help():
    print(HELP)


def show_usage():
    print("MealPrepBox - Meal Prep Planner")
    print("Usage: mealprepbox.py <command> [options]")
    print("Run 'mealprepbox.py help' for full documentation.")
