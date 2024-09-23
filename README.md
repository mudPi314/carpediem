# carpediem
A python implementation of Zvi's resource-management solitare game, [Carpe Diem](https://thezvi.wordpress.com/2015/03/17/carpe-diem-the-optimization-game-level-1/).

To run it, just open a terminal, clone the repo, `cd` into the folder, and run `carpediem.py`.
```
git clone https://github.com/mudPi314/carpediem.git
cd carpediem
python3 carpediem.py
```
The only dependency is Python 3. For rules, see the link above. I modified the rules very slightly, implementing the suggestion in [this comment](https://thezvi.wordpress.com/2015/03/17/carpe-diem-the-optimization-game-level-1/#comment-2), so it is the last card drawn, rather than the first, that is used to determine whether or not you drain an extra energy at the start of the day.

I coded this in one afternoon, so it is kind of shitty and probably has bugs that I haven't found. Feel free to pull request if you want to make it less shitty.
