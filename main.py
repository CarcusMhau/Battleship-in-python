def main():
    window = arcade.Window(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)
    start_view = Insturctions()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
