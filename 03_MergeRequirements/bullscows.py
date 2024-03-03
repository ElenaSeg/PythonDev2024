from pathlib import Path
from argparse import ArgumentParser
from collections import Counter
import typing
from random import choice
import requests


def ask(prompt: str, valid: typing.List[str]) -> str:
    while True:
        print(prompt)
        guess = input().strip()
        if guess not in valid:
            print('Такого слова нет в словаре')
            continue
        else:
            return guess
    
def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def bullscows(guess: str, secret: str) -> typing.Tuple[int, int]:
	if len(guess) != len(secret):
		raise ValueError("guess and secret strings must be the same length")
	bulls = sum(guess == secret for guess, secret in zip(guess, secret))
	common = Counter(guess) & Counter(secret)
	cows = sum(common.values())
return bulls, cows

def gameplay(ask: typing.Callable, inform: typing.Callable, words: typing.List[int]) -> int:
    secret = choice(words)
    attempts = 0
    while True:
        attempts += 1
        guess = ask("Введите слово: ", words)
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        if bulls == len(secret):
            break
    return attempts

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('dictionary', help='Path/URL with list of words')
    parser.add_argument('length', nargs='?', type=int, default=5, help='Word length')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if Path(args.dictionary).exists():
        with Path(args.dictionary).open() as f:
            dictionary = [line.strip() for line in f.readlines()]
    else:
        with requests.get(args.dictionary) as r:
            dictionary = [word.strip() for word in r.text.split()]

    if args.length:
        dictionary = [word for word in dictionary if len(word) == args.length]
    
    attempts = gameplay(ask, inform, dictionary)
    print(f'Game ends with {attempts} attempts')