# Instagram Username Checker

এই ফাইলটি নতুন ব্যবহারকারীদের জন্য গাইডলাইন। এখানে বলা আছে কীভাবে প্রোগ্রামটি ব্যবহার করতে হবে।

---

## ফোল্ডার স্ট্রাকচার

```
insta_checker/
│
├── main.py
└── user.txt
```

- `main.py` : Python স্ক্রিপ্ট যা username চেক করে।
- `user.txt` : username তালিকা। প্রতি লাইনে একটি করে username লিখবে।

---

## ধাপ ১: Python ইনস্টল করা

1. CMD খুলে লিখো:
   ```
   python --version
   ```
2. যদি version দেখায়, Python আছে।
3. না হলে [Python ডাউনলোড](https://www.python.org/downloads/) করে ইনস্টল করো।
4. ইনস্টল করার সময় **Add Python to PATH** টিক দিতে হবে।

---

## ধাপ ২: দরকারি লাইব্রেরি ইনস্টল

CMD তে লিখো:
```
pip install requests colorama
```

---

## ধাপ ৩: Username লেখা

`user.txt` খুলে username গুলো লিখো।
উদাহরণ:
```
itsnasim00
shipreha35587
sumaiya5808islam
sumafiya5808islam
```

---

## ধাপ ৪: প্রোগ্রাম চালানো

1. CMD তে ওই ফোল্ডারে যাও:
   ```
   cd Desktop\insta_checker
   ```
2. চালাও:
   ```
   python main.py
   ```

---

## আউটপুটের মানে

- **ACTIVE** : username এখনো Instagram-এ অ্যাকাউন্টে আছে (সবুজ)
- **AVAILABLE** : username ফ্রি, নেওয়া যাবে (সায়ান/সবুজ-সাইড)
- **NOT_AVAILABLE** : আগে ব্যবহার হয়েছে কিন্তু এখন ব্যাড/ডিসেবল (লাল)
- **UNKNOWN** : নিশ্চিত বলা যাচ্ছে না (হলুদ)

---

## প্রোগ্রামের বৈশিষ্ট্য

- Multi-threaded, ফাস্ট চেক
- Delay555: প্রতি চেকের পরে 5.5 সেকেন্ড অপেক্ষা
- Color-coded আউটপুট
- শেষ হলে CMD বন্ধ হয় না, Enter চাপা পর্যন্ত অপেক্ষা করে

---

## সংক্ষিপ্ত ব্যবহার

1. `user.txt` এ নাম লিখো
2. `python main.py` চালাও
3. রেজাল্ট দেখো
4. Enter চাপো তারপর CMD বন্ধ হবে

