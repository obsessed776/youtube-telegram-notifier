-- Stores YouTube channels being tracked.
CREATE TABLE youtube_channels(
    id INTEGER PRIMARY KEY,
    channel_id TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    last_video_id TEXT DEFAULT NULL
);

-- Stores Telegram chats subscribed to notifications.
CREATE TABLE telegram_chats(
    id INTEGER PRIMARY KEY,
    telegram_chat_id BIGINT NOT NULL,
    title TEXT NOT NULL
);

-- Links YouTube channels with Telegram chats.
CREATE TABLE subscriptions(
    id INTEGER PRIMARY KEY,
    youtube_channel_id INTEGER NOT NULL,
    telegram_chat_id INTEGER NOT NULL,

    FOREIGN KEY (youtube_channel_id) REFERENCES youtube_channels(id),
    FOREIGN KEY (telegram_chat_id) REFERENCES telegram_chats(id),

    UNIQUE (youtube_channel_id, telegram_chat_id)
);
