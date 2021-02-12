## Usage

This is a simple script that will email you the stats on your MusicNotes page (I.e. how many people are buying your scores and how much money you've earned).

To use it:

1. Download the script to your computer and enter your credentials on line 12:

```python
login("", "")
```

2. On **line 33**, update `num_pieces` to the number of pieces that you want to see in your email; you will receive the statistics for that number of pieces.

3. On **line 72**, edit the correct SMTP server information to connect it to your email. I recommend creating a new email specifically for this purpose. You will need to sign in below on **lines 74 and 75**

4. Create a crontab or schedule this script to run everyday. Mine is set to run at 7am every morning.

   