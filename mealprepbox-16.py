# === Stage 16: Add argparse support for the most common commands ===
# Project: MealPrepBox
import argparse

def main():
    parser = argparse.ArgumentParser(description="MealPrepBox - Meal Prep Planner")
    subparsers = parser.add_subparsers(dest="command")

    prep_parser = subparsers.add_parser("prep", help="Prepare a meal batch")
    prep_parser.add_argument("recipe", help="Recipe name")
    prep_parser.add_argument("--portions", type=int, default=1, help="Number of portions")
    prep_parser.add_argument("--container", default="standard", help="Container type")

    freeze_parser = subparsers.add_parser("freeze", help="Store batch in freezer")
    freeze_parser.add_argument("recipe", help="Recipe name")
    freeze_parser.add_argument("--by", type=int, default=1, help="Number of weeks to freeze")

    rehearse_parser = subparsers.add_parser("reheat", help="Reheat a frozen meal")
    rehearse_parser.add_argument("recipe", help="Recipe name")
    rehearse_parser.add_argument("--method", default="microwave", help="Reheating method")

    show_parser = subparsers.add_parser("show", help="Show meal plan summary")
    show_parser.add_argument("--type", choices=["prep", "freeze", "reheat"], help="Filter by type")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return
    print(f"[MealPrepBox] {args.command}: {getattr(args, 'recipe', args.command)}")

if __name__ == "__main__":
    main()
