async function main(args) {
  const gameUrl = args.url;
  const webhookUrl = args.DISCORD_WEBHOOK_URL; // From environment variable

  if (!gameUrl) {
    return {
      statusCode: 400,
      body: { error: "Missing game URL" },
    };
  }

  try {
    const response = await fetch(webhookUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        content: `🎮 New game lobby!\nJoin here: ${gameUrl}\n\nClick the link to join the game!`,
        username: "Game Invite Bot",
      }),
    });

    if (!response.ok) {
      throw new Error(`Discord webhook failed: ${response.statusText}`);
    }

    return {
      statusCode: 200,
      body: { message: "Invite sent successfully!" },
    };
  } catch (error) {
    console.error("Error sending Discord webhook:", error);
    return {
      statusCode: 500,
      body: { error: "Failed to send invite" },
    };
  }
}
