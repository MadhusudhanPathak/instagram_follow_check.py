import os
import json
import csv

def extract_users_with_links(data_list):
    users = {}
    for entry in data_list:
        try:
            string_data = entry["string_list_data"][0]
            username = string_data["value"]
            link = string_data["href"]
            users[username] = link
        except (KeyError, IndexError):
            continue
    return users

# Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))
followers_path = os.path.join(script_dir, 'followers.json')
following_path = os.path.join(script_dir, 'following.json')

# Load followers.json
with open(followers_path, 'r') as f:
    followers_data = json.load(f)
followers = extract_users_with_links(followers_data)

# Load following.json
with open(following_path, 'r') as f:
    following_raw = json.load(f)
following_data = following_raw.get("relationships_following", [])
following = extract_users_with_links(following_data)

# Determine relationships
not_following_back = {
    username: link for username, link in following.items()
    if username not in followers
}

not_followed_back_by_you = {
    username: link for username, link in followers.items()
    if username not in following
}

# Display summary
print(f"\n👤 You follow: {len(following)}")
print(f"👥 They follow you: {len(followers)}")

print(f"\n🚫 Not following you back: {len(not_following_back)}")
for i, (username, link) in enumerate(sorted(not_following_back.items()), 1):
    print(f"{i}. {username} → {link}")

print(f"\n🔁 You don’t follow back: {len(not_followed_back_by_you)}")
for i, (username, link) in enumerate(sorted(not_followed_back_by_you.items()), 1):
    print(f"{i}. {username} → {link}")

# --- Save TXT ---
def save_txt(data_dict, filename):
    with open(os.path.join(script_dir, filename), 'w', encoding='utf-8') as f:
        for username, link in sorted(data_dict.items()):
            f.write(f"{username}: {link}\n")

save_txt(not_following_back, 'not_following_back.txt')
save_txt(not_followed_back_by_you, 'not_followed_back_by_you.txt')

# --- Save CSV ---
def save_csv(data_dict, filename):
    with open(os.path.join(script_dir, filename), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username', 'Instagram Link'])
        for username, link in sorted(data_dict.items()):
            writer.writerow([username, link])

save_csv(not_following_back, 'not_following_back.csv')
save_csv(not_followed_back_by_you, 'not_followed_back_by_you.csv')

# --- Confirm outputs ---
print("\n✅ Files saved:")
print("  ➤ not_following_back.txt")
print("  ➤ not_followed_back_by_you.txt")
print("  ➤ not_following_back.csv")
print("  ➤ not_followed_back_by_you.csv")