import requests


def main(args):
    url = args.get("url")
    if not url:
        return {"error": "Missing game URL"}

    webhook_url = args.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        return {"error": "Missing Discord webhook URL"}
    avatar_url = args.get(
        "avatar_url",
        "https://i1.rgstatic.net/ii/profile.image/11431281236739734-1713351820088_Q512/Ziga-Lesar-2.jpg",
    )

    try:
        response = requests.post(
            webhook_url,
            json={
                "content": f"🎮 New game lobby!\nJoin here: {url}\n\nClick the link to join the game!",
                "username": "Game Invite Bot",
                "avatar_url": avatar_url,
            },
        )
        response.raise_for_status()

        return {"message": "Invite sent successfully!"}
    except requests.RequestException as e:
        print(f"Error sending Discord webhook: {e}")
        return {"error": "Failed to send invite"}
