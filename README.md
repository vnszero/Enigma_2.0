# Enigma_2.0
An encryption device based on Enigma from WWII

## What is the difference here?
Enigma 2.0 don't use a shuffle combination based on plugs and mixes.
It uses Cesar Code plus fake letters plus config letters in the middle 
of the message. There's not so many combinations as the old model but 
it makes big mess. Even small and commun sentences can become large 
and harder to decrypt, because it's difficult to say what is fake, what 
is machine config or what is message itself.

## The problems
How was said, the config is unique per code and sent along with the 
message. So anyone with the code could find the answer, but it's not
so easy, only a person who understand what it means could decrypt in time.
I know what you're thinking: "... and someone with a Turing Machine?".
Of course, Enigma 2.0 belongs to the Turing Paradigm, so other machine
on the same paradigm can solve, but it still hard logic problem.

## Could be stronger?
Yes. The current model accept 90 different characters based on ASCII
and the setting terms are at the beginning of every code. An improve
can add new setting terms that makes mores shuffles with the already
defined settings or with the message itself.

## Decryption method
It just backtracks based on the terms of the settings.

## Author
[VINICIUS N. SILVA](https://github.com/vnszero)

## Goal
Try to understand Turing Machine and explore its limits.