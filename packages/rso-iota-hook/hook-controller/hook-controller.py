import requests


def main(args):
    url = args.get("url")
    if not url:
        return {"error": "Missing game URL"}

    webhook_url = args.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        return {"error": "Missing Discord webhook URL"}

    try:
        response = requests.post(
            webhook_url,
            json={
                "content": f"🎮 New game lobby!\nJoin here: {url}\n\nClick the link to join the game!",
                "username": "Game Invite Bot",
            },
        )
        response.raise_for_status()

        return {"message": "Invite sent successfully!"}
    except requests.RequestException as e:
        print(f"Error sending Discord webhook: {e}")
        return {"error": "Failed to send invite"}


# async function main(args) {
#   const gameUrl = args.url;
#   const webhookUrl = args.DISCORD_WEBHOOK_URL; // From environment variable

#   if (!gameUrl) {
#     return {
#       statusCode: 400,
#       body: { error: "Missing game URL" },
#     };
#   }

#   try {
#     const response = await fetch(webhookUrl, {
#       method: "POST",
#       headers: {
#         "Content-Type": "application/json",
#       },
#       body: JSON.stringify({
#         content: `🎮 New game lobby!\nJoin here: ${gameUrl}\n\nClick the link to join the game!`,
#         username: "Game Invite Bot",
#       }),
#     });

#     if (!response.ok) {
#       throw new Error(`Discord webhook failed: ${response.statusText}`);
#     }

#     return {
#       statusCode: 200,
#       body: { message: "Invite sent successfully!" },
#     };
#   } catch (error) {
#     console.error("Error sending Discord webhook:", error);
#     return {
#       statusCode: 500,
#       body: { error: "Failed to send invite" },
#     };
#   }
# }
