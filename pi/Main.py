import Gaitmate

def main():
    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 25)
    controller.execute()

main()
