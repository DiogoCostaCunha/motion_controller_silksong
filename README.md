# Silksong Body Motion Controller (aka 3-Player Silksong) 🏃⚔️

This is the code for the motion controller setup used in my Silksong videos! You can now play Silksong using your body—with friends or all by yourself.

### Watch the Series:
| [ ![Part 1](https://github.com/user-attachments/assets/736fed8e-5ad8-4156-b433-4fb6d7bf5bdc) ](https://youtu.be/TjnGbk6SaU0?si=xk7sMdGfoCOF2a3l) | [ ![Part 2](https://github.com/user-attachments/assets/afcbb220-8a85-46c5-b804-c2ad36980ff5) ](https://youtu.be/D0kf4gtPdv) | [ ![Part 3](https://github.com/user-attachments/assets/94065b55-a463-4533-854b-4e61585f7b97) ](https://youtu.be/RluS-Kx0iQg?si=0uz-IKpB8Az1CQ1f) |
|:---:|:---:|:---:|
| [**Part 1: Moss Mother**](https://youtu.be/TjnGbk6SaU0?si=xk7sMdGfoCOF2a3l) | [**Part 2: Bell Beast**](https://youtu.be/D0kf4gtPdv) | [**Part 3: Deep Docks Lace**](https://youtu.be/RluS-Kx0iQg?si=0uz-IKpB8Az1CQ1f) |

---

## 🧠 How It Works

This project uses Computer Vision to detect specific colors (like a green screen cloth) within "trigger zones" on your camera feed. When a color is detected in a specific zone, the script simulates a keypress on your keyboard.

To better understand the logic please check out **[this tutorial video](link-still-to-be-inserted)**.

---

## ⚙️ Setup Instructions

> **Note:** Requires Python **3.10+**. If you need help installing Python, [check out this tutorial](https://www.youtube.com/watch?v=YKSpANU8jPE).

1.  **Clone** or download this repository to your machine.
2.  Create and activate a [Python virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Customize Controls:** Open `control_settings.json` to map your zones to specific keys. If you want one zone to trigger multiple keys, you can use a list: `["a", "x"]`. Refer to the [tutorial video](link-still-to-be-inserted) for a deep dive.
5.  **Generate the Grid:** Run the following command to save your control layout:
    ```bash
    python grid.py
    ```
    You can verify the setup by checking the generated `control_grid.png`.
6.  **Start Capturing:** Run the main script to start the motion detection:
    ```bash
    python main.py
    ```
7.  **Play Silksong:** Ensure the Silksong window is **focused** (active), or the controls will not be detected. 
    * *Pro Tip:* Use a second monitor to watch your control feed while you play, or run Silksong in **Windowed Mode**.

---

## 💡 Essential Items

For the best experience, you will need:

1.  **A Laptop/PC:** To run the scripts and process footage in real-time. The script uses basic CV algorithms, so most modern machines handle it easily!
2.  **A Camera:** A standard webcam (I used a Logitech) pointed at your play area.
3.  **Green Screen Cloth:** I used a bright green cloth from Amazon. This color is easiest for the computer to distinguish from skin or clothing.
    * *Note:* You can modify `settings.json` to use other colors, but green is the most reliable.
4.  **Good Lighting:** A well-lit space is key for the camera to track your movements well and clearly distinguish colors.

---

## 🌍 Share it with the world!

I’m really curious to see how you use this! Feel free to [join my Discord Community](https://discord.gg/hSva6VG9H8) and share your gameplay clips in the `#general` chat. I might even feature your videos in a future project!

## Support My Channel 🚀

I make weird and wonderful projects at the crossroads of AI, hardware, and chaotic fun. 

If you enjoyed this project, please consider **[subscribing to my YouTube channel](https://www.youtube.com/channel/UCqnIZIGyH6NgJ8OkJAvZyKg?sub_confirmation=1)**. Your support helps me keep doing this stuff!
