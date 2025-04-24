# 🎬 YouTube Video Downloader (Flask + yt-dlp)

এই প্রজেক্টটি একটি ইউটিউব ভিডিও ডাউনলোডার, যেটি বানানো হয়েছে Python Flask এবং yt-dlp ব্যবহার করে। এটি YouTube Shorts সাপোর্ট করে এবং কুকিজ ফাইল ব্যবহার করে প্রাইভেট/লগইন প্রয়োজনীয় ভিডিও ডাউনলোড করতে পারে।

---

## ✅ ফিচারসমূহ

- 🎯 যেকোনো ইউটিউব ভিডিও ডাউনলোড করুন নির্দিষ্ট resolution সহ (Best, 720p, 480p, 360p)
- 🎯 YouTube Shorts লিংককে অটোমেটিক ওয়াচ লিংকে কনভার্ট করে
- 🎯 কুকিজ ফাইল দিয়ে প্রাইভেট / লগইন-চাওয়া ভিডিও সাপোর্ট
- 🎯 অডিও ও ভিডিও মার্জ করে MP4 ফাইল বানায়
- 🎯 সুন্দর এবং সহজ UI (HTML ফর্ম)
- 🎯 ইউনিক ফাইলনেম (UUID) দিয়ে ফাইল সেভ

---

## 🧱 প্রজেক্ট স্ট্রাকচার

your_project/ ├── app.py ├── templates/ │ └── index.html ├── downloads/ ├── cookies/ │ └── cookies.txt └── README.md

yaml
Copy
Edit

---

## ⚙️ ইনস্টলেশন ও রান করার নিয়ম

প্রথমে প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:

```bash
pip install flask yt-dlp werkzeug
অথবা requirements.txt দিয়ে:

bash
Copy
Edit
pip install -r requirements.txt
তারপর Flask অ্যাপ রান করুন:

bash
Copy
Edit
python app.py
ব্রাউজারে যান:
📍 http://localhost:5000

🍪 কুকিজ ফাইল কীভাবে যোগ করবেন?
কিছু ভিডিও ডাউনলোড করতে লগইন থাকা লাগে (যেমন: age-restricted/private):

আপনার ব্রাউজারে লগইন করুন (YouTube-এ)

এই Chrome এক্সটেনশনটি ইনস্টল করুন:
🔗 Get cookies.txt

youtube.com থেকে <mark> netscape </mark> cookies export করুন

cookies ফাইলটি cookies/cookies.txt নামে সেভ করুন

অ্যাপটি আবার রান করুন

yt-dlp স্বয়ংক্রিয়ভাবে কুকিজ ফাইল ব্যবহার করবে।

