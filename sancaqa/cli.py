import argparse


def parse_command_line():
    parser = argparse.ArgumentParser(
        description='sancaQA description',
    )
    parser.add_argument('--version', action='version', version='0.0.1')
    return parser.parse_args()


def main():
    # args = parse_command_line()
    print("Halo Juragan")


if __name__ == '__main__':
    main()
