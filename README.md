# Just Read the Source Code
and use it.
it is easy to understand
  
  AVD2.py is the newest edition.

</br></br>

# Simple Intro
in 
    <pre><code>class R:</code></pre>
+ the `__init__()` function is to init all the parts(maybe) in the `root` window.
+ the `choose()` function is to choose file that includes your plans.
+ the `write()` function is to write the current plans that show in the `root` window to the file that you have selected in the function `choose()`.
+ the `read()` function is to import a new sheet of plans from the file you have chosen by `choose()`.
+ the `Del()` function is to del sth. you selected in the listbox.(there's a counter to record the number of your plans)
+ the `Add()` function will make a new window named `nrot` to get input plan infos and add it to the listbox.
+ the `Apply()` function is to confirm that the input infos.(in the `nrot`)
+ the `bfollow() tfollow()` functions are to make sure you click one of them and the both your plan and times will be lightened.
+ the `bscry() bscrx() tscry() tscrx() xview() yview()` functions are to connect with the scrollbar, make sure they can scroll synchronously.
+ the `test()` function is for test.(alse read file)
+ the `status` `staini` is to control that when the subwindow `nrot` is exists that other parts in the `root` isn't availabled.
+ the `loop()` is for loop.

in
    <pre><code>if __name__ == "__main__":</pre></code>
+ init an R object and loop it.(the mainloop is here!)

</br></br>

# Thanks & Sorries
you guys see that some names of the functions is capitalized, sorry about that, idont want to change it.
Thanks to StackOverFlow's mina.[ website here! ](https://stackoverflow.com/questions/4066974/scrolling-multiple-tkinter-listboxes-together)
Thanks to MarkGarway and Dear Miss.Strawberry.They support me.

</br></br>

# LICENSE
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)


