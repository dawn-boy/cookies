## What is it?
This program helps you to use your kindle highlights with the fortune tool in linux.

## Prerequisites
You gotta have,
- [fortune](https://wiki.archlinux.org/title/Fortune)
### optional
- [cowsay](https://archlinux.org/packages/extra/any/cowsay/)
- [neofetch](https://github.com/dylanaraps/neofetch)
## Get creative, Try some of these!
- Plain and Simple (Personal fav)
![1](https://github.com/dawn-boy/cookies/assets/143283986/1248a4cd-8346-4014-a732-c54590c73207)
```sh
# Add this to your .bashrc file
eval "fortune path/to/cookies"
```
- Let the Dragon speak!
![2](https://github.com/dawn-boy/cookies/assets/143283986/0fdcc2a7-6a4b-4f1c-9550-1ff210068157)
```sh
eval "fortune /path/to/cookies | cowsay -f dragon"
```
- Integrate it with neofetch
![3](https://github.com/dawn-boy/cookies/assets/143283986/575e3c9d-a22c-41af-ae84-a1ec17663bd6)
```sh
eval 'neofetch --ascii "$(fortune .cookies/cookies | cowsay -f dragon)"'
```


# How To Use
1) Make sure you have your kindle highlights in the same folder with the name "My Clippings.txt"
2) Just run the Program and it'll output a fortune-friendly file
3) Enjoy your Highlights with fortune!
