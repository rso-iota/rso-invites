# RSO Invites

A webhook service for sending game lobby invites to Discord.

## Usage

Send a POST request to the service endpoint with your game invite data in JSON format:

```json
{
    "url": "string",        // Required: URL of the game lobby
    "avatar_url": "string"  // Optional: Custom avatar URL for the Discord bot
}
```

### Required Parameters
- `url`: The URL of the game lobby that players should join

### Optional Parameters
- `avatar_url`: A custom avatar URL for the Discord bot (defaults to a predefined image)

### Response

Success response:
```json
{
    "message": "Invite sent successfully!"
}
```

Error response:
```json
{
    "error": "Missing game URL"
}
```
or
```json
{
    "error": "Failed to send invite"
}
```

The service will send a message to Discord with:
- A game controller emoji 🎮
- The game lobby URL
- Instructions to click the link
- Using "Game Invite Bot" as the webhook name

Note: The Discord webhook URL is configured through environment variables and is not included in the request.