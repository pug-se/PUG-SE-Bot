import gdgajubot.__main__

from .bot import PugSeBot

# monkey patching to reuse the CLI interface
gdgajubot.__main__.GDGAjuBot = PugSeBot


def main():
    gdgajubot.__main__.main()


if __name__ == '__main__':
    main()
