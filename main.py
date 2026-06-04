from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

BOT_TOKEN = "8752299691:AAH_eeBpCdv1I4pSc5rdki0nlazW5v638fU"

CHANNEL = "@kdediting18"
CHANNEL_LINK = "https://t.me/kdediting18"

GROUP_LINK = "https://t.me/kdeditingchat"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📢 Join Channel",
                url=CHANNEL_LINK
            )
        ],
        [
            InlineKeyboardButton(
                "✅ Verify",
                callback_data="verify"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📢 પહેલા Channel Join કરો અને પછી Verify બટન દબાવો.",
        reply_markup=reply_markup
    )


async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    try:

        member = await context.bot.get_chat_member(
            CHANNEL,
            user_id
        )

        if member.status in [
            "member",
            "administrator",
            "creator"
        ]:

            keyboard = [
                [
                    InlineKeyboardButton(
                        "👥 Join Group",
                        url=GROUP_LINK
                    )
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            await query.message.reply_text(
                "✅ Verification Successful!\n\n🎉 હવે Group Join કરો.",
                reply_markup=reply_markup
            )

        else:

            await query.message.reply_text(
                "❌ પહેલા Channel Join કરો."
            )

    except Exception as e:
        print(e)

        await query.message.reply_text(
            "❌ પહેલા Channel Join કરો."
        )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CallbackQueryHandler(
        verify,
        pattern="verify"
    )
)

print("✅ Force Subscribe Bot Started")

app.run_polling()
