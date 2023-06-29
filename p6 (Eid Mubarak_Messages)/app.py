from flask import Flask, render_template
import random

app = Flask(__name__)

messages = [
    "Eid Mubarak! May the blessings of Eid bring happiness, peace, and prosperity to your life.",
    "Wishing you a joyous and blessed Eid filled with love, laughter, and togetherness.",
    "May this Eid bring joy and success to your life. Eid Mubarak!",
    "Sending you warm wishes on the auspicious occasion of Eid ul Adha. Have a blessed and happy Eid.",
    "May the divine blessings of Allah fill your home and heart with peace, happiness, and prosperity. Eid Mubarak!",
    "On this special day, I pray that Allah's blessings and divine grace be showered upon you. Eid Mubarak!",
    "Wishing you and your family a joyous and peaceful Eid. May Allah accept your good deeds and forgive your sins.",
    "May this Eid bring endless blessings and true joy to your life. Eid Mubarak!",
    "Sending warm wishes and happiness your way on this blessed occasion. Eid Mubarak!",
    "May the magic of Eid bring lots of happiness, joy, and prosperity to your life. Eid Mubarak!",
    "Wishing you a blessed and memorable Eid full of love, laughter, and cherished moments.",
    "May the light of Allah's love and guidance shine upon you and your family. Eid Mubarak!",
    "May the blessings of Allah be with you and your loved ones. Eid Mubarak!",
    "Wishing you a blessed Eid overflowing with love, happiness, and success.",
    "May Allah grant all your wishes and fill your life with happiness and prosperity. Eid Mubarak!",
    "Eid Mubarak to you and your family. May this day bring joy and love to your heart and create beautiful memories.",
    "Sending you warm wishes on Eid. May Allah bless you and your family with happiness and peace.",
    "May the joy of Eid ul Adha fill your heart and home with love, laughter, and togetherness.",
    "Wishing you a delightful Eid full of blessings and wonderful moments. Eid Mubarak!",
    "May this Eid bring you good health, happiness, and success in everything you do. Eid Mubarak!",
]

@app.route("/")
def generate_message():
    random_message = random.choice(messages)
    return render_template("message.html", message=random_message)

if __name__ == "__main__":
    app.run()
