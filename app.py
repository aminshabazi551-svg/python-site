from flask import Flask, render_template

app = Flask(__name__)

members = [
    {
        "name": "صبا پایتون",
        "role": "Team Lead",
        "skill": "امنیت",
        "text": "هماهنگی تیم و بررسی موضوعات امنیتی، از ایده اولیه تا نتیجه نهایی."
    },
    {
        "name": "جهان بانو پایتون",
        "role": "Web Developer",
        "skill": "توسعه سایت",
        "text": "ساخت و توسعه رابط‌های وب با تمرکز روی ظاهر تمیز و تجربه کاربری."
    },
    {
        "name": "شاهان پایتون",
        "role": "Network",
        "skill": "تست فشار و تاب‌آوری شبکه",
        "text": "بررسی رفتار سرویس‌ها زیر فشار و پیدا کردن نقاطی که نیاز به بهبود دارند."
    },
    {
        "name": "فائزه پایتون",
        "role": "Security Tester",
        "skill": "تست نفوذ",
        "text": "بررسی امنیت سیستم‌ها در محیط‌های مجاز و ثبت دقیق مشکلات پیدا شده."
    }
]

@app.route("/")
def index():
    return render_template("index.html", members=members)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
