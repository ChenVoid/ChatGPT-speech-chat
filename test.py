# coding: utf-8
import openai

from play_mp3 import play_mp3
from polly import request_from_polly
import textwrap

openai.api_key = "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"


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()


if __name__ == '__main__':
    while True:
        input_message = input("Q: ")
        output_message = generate_response(input_message)
        file = open('test.txt', 'w')
        file.write(output_message)
        file.close()
        request_from_polly(output_message)
        print(textwrap.fill(output_message, 100))
        play_mp3("test.mp3")
