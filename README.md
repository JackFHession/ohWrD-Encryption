<h1> ohWrD Encryption Program </h1>
<h2> An optionally self-destructive byte-scrambling encryption program. </h2>

<p> This program functions by taking in a key as an ASCII value and scrambling your zip file's byte composition to render it unusable.</p>

<p> If an incorrect password is typed in, the program will proceed to de-scramble the file by its values, but consequently make the zip file an unusable and unobtainable mess. It can be reversed, obviously, if you know how the code works. </p>

<p> It is programmed to trigger a hidden .safe.py file, which I have not included for obvious reasons (its dangerous), you can program it to do whatever you like.</p>

<p> This code will function properly even without the .safe.py file, as that's the final line of code and so it won't interrupt anything involving the encryption/decryption </p>


<h2> Usage (encryption) </h2>

**1.** Create a folder and throw in whatever you wish to encrypt.\n
**2.** Zip the folder and make sure that there is no .ohwrd file present.\n
**3.** Run the program, it asks for a password to use as ASCII key values.\n
**4.** It will save your scrambled/encrypted zip file as "gallifrey.ohwrd" - keep this file.\n
**5.** Delete the original zip file.\n
\n
<h2> Usage (decryption) </h2>

Do you wonder why I named it the Dr Who encryption in reverse, or why it saves your encrypted zip as Gallifrey.ohwrd (.drwho backwards)?

That's because the file will continue to transform into a zip file, even if your password is incorrect - if the password is incorrect, that'll seriously corrupt or regenerate your file into an unreadable and bad zip file.

Sorry, lol.

**1.** Make sure your Gallifrey.ohwrd file is in the same directory as run.py, and that there's no zip files present.\n
**2.** Enter your password, same interface.\n
**3.** It'll use the ASCII values of your entered password to unscramble the zip file, if correct then the zip file will be fully restored - if incorrect, it'll create an awfully corrupted binary file in a zip shell.\n
**4.** If password is correct, your zip file is fully restored, just delete the Gallifrey.ohwrd if you want.\n
