# Silksong Body Motion Controller (aka 3-Player Silksong) 🏃⚔️

This is the code for the motion controller setup used in these Silksong videos!
- [Can We Beat Silksong Using Our Bodies? (Part 1)](https://youtu.be/TjnGbk6SaU0?si=xk7sMdGfoCOF2a3l)
- [Can We Beat Silksong Using Our Bodies? (Part 2)](https://youtu.be/D0kf4gtPvl4?si=t_TzcQt9sDoyfPdv)
- [Can We Beat Silksong Using Our Bodies? (Part 3)](https://youtu.be/RluS-Kx0iQg?si=0uz-IKpB8Az1CQ1f)

You can now play Silksong using your body, with your friends or even all by yourself!

## 🧠 How It Works

To better understand it  please check out [this tutorial video](link still to be inserted).

## ⚙️ Setup Instructions

> Requires Python **3.10+**. [Here's a tutorial on how to do it](https://www.youtube.com/watch?v=YKSpANU8jPE).

1. **Clone** or download this repository.
2. Create and activate a [python virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
3. Install the requirements ```pip install -r requirements.txt```
4. Modify the ```control_settings.json``` to customize the control setup for your needs. Please check [the tutorial video](link still to be inserted). If you really want you can assign more than one key to a rectangle, like so ```['a', 'x']```.
5. Run ```python grid.py``` to save the new control setup. You can check it out in the ```control_grid.png```.
6. Run ```python main.py``` to start capturing footage.
7. Now just start Silksong and ensure that Silksong is the focused window or the controls will not be detected. You can use a separate screen to simultaneously be able to play and watch the controls or you can put the Silksong window in windowed mode.

## 💡 Essential Items

For this to work well you will need:
1. A laptop to run the scripts and process the incoming footage in real-time. Don't worry, the script uses basic Computer Vision algorithms so your machine should handle it well!
2. A camera connected to your laptop. In the videos I was using a Logitech camera but any camera should suffice. It just needs to be pointed at where you will be playing.
3. A green screen cloth. I bought mine on amazon for video editing purposes. That color is the best because it is not easily confused with skin or clothes. In theory you can modify ```settings.json``` file to adapt for different color ranges. It might just not work as well.
4. A well illuminated space. Yes, to move freely! Specially if you're playing with others.

## 🌍 Share it with the world!

I am really curious about watching other people playing Silksong this way! Feel free to [join my Discord Community](https://discord.gg/hSva6VG9H8) and share videos of you playing it on the #general chat. I might even make a video featuring other people playing Silksong this way! 

## Support My Channel 🚀

I make weird and wonderful projects at the crossroads of AI, hardware, and chaotic fun.

If you found this helpful, enjoyed the Silksong videos and are ready for more madness please consider [subscribing to my YouTube channel](https://www.youtube.com/channel/UCqnIZIGyH6NgJ8OkJAvZyKg?sub_confirmation=1). Your support helps me keep doing this stuff!
