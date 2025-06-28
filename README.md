# Instagram Follow Checker 🕵️‍♂️

A clean, offline, and fully transparent Python tool to **identify who doesn’t follow you back on Instagram**, and who you don’t follow back, based on your downloaded data from Instagram itself.

---

## 🧭 Why I Built This

Instagram **does not natively provide** a way to see who doesn't follow you back. While many third-party apps claim to offer this, they often:
- Require you to log in with your Instagram account (risking security)
- Misuse or sell your data
- Are filled with ads or incomplete results

This tool was created to give **a safe, offline, and fully verifiable way** to do it, using only your downloaded Instagram data.

---

## 🔍 What This Tool Does

Using your official `followers.json` and `following.json` from Instagram, this script identifies:

- 🚫 People you follow, who **don't follow you back**
- 🔁 People who follow you, but you **don’t follow back**
- ✅ Outputs both lists in:
  - Console
  - `.txt` files (clean, readable)
  - `.csv` files (with username + Instagram link)

---

## 📥 How to Get Your Instagram Data

1. Go to: [**Instagram → Settings → Your Activity → Download Your Information**](https://www.instagram.com/download/request/)
2. Request your data in **JSON format**
3. After you receive the ZIP file:
   - Extract it
   - Find the following files:
     - `followers.json` → usually in `followers_and_following/`
     - `following.json` → usually in `followers_and_following/`

---

## 🚀 How to Use

### 1. 📁 Place These Files in the Same Folder:
- `instagram_follow_check.py` (the script)
- `followers.json`
- `following.json`

### 2. 🐍 Run the Script:
```bash
python instagram_follow_check.py
