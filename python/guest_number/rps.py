def Welcome(name):
    msg = f"{name}"
    print("Welcome to the game, ",msg)

def Xuat():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )
    args = parser.parse_args()
    Welcome(args.name) 