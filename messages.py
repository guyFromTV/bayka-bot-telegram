from telebot import formatting

START_MESSAGE = "<b>Hello!</b> Nice to see you <u>here</u>. <i>How can I assist you?</i>"
HELP_MESSAGE = """Here are this bot's commands:

- /start - start bot
- /help - send help message
- /joke - random joke
- /joke2 - random 2 part joke
- /rub_to_azn 100 - convert 100 RUB to AZN
- /cvt 100 USD - convert 100 USD to AZN
- /cvt 100 RUB USD - convert 100 RUB to USD
"""

FORWARD_WARNING = "Send forwarded command might be dangerous. Don't do it!"

REPLY_TEXT = "You <b>replied</b> to <u>this message</u> type : "

SECRET_TEXT = "Your secret key is ..."

SECRET_TEXT_FOR_NOT_ADMIN = "You are not admin, so...   NO!"

HTML_TEXT = """
<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=5352742389">inline mention of a user</a>
<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
<blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>
<blockquote expandable>Expandable block quotation started\nExpandable block quotation continued\nExpandable block quotation continued\nHidden by default part of the block quotation started\nExpandable block quotation continued\nThe last line of the block quotation</blockquote>
"""

ENTITIES_TEXT = "Message has entities"

BYE_MESSAGE = "See you soon!"

ABOUT_INFO_CAPTION = "That's it!"

CONVERT_RUB_TO_AZN_HOW_TO = formatting.format_text(
    "Please, indicate the argument for conversion, for example:",
    formatting.hcode("/rub_to_azn 100"),
    separator=" ",
)

CVT_CURRENCIES_HOW_TO = formatting.format_text(
    "Please, indicate the arguments for conversion to AZN, for example:",
        formatting.hcode("/cvt 100 USD"),
    )



WRONG_ARG_FOR_CNVRT = "Incorrect argument:"


def rub_to_azn_conversion_message(rub_amount, azn_amount):
    return conversion_message(
        from_amount=rub_amount,
        to_amount=azn_amount,
        from_currency='rub',
        to_currency='azn',
    )


def conversion_message(from_amount, to_amount, from_currency, to_currency):
    text = formatting.format_text(
        formatting.hcode(f"{from_amount:,}"),
        f"{from_currency.upper()} is approximately",
        formatting.hcode(f"{to_amount:,.2f}"),
        to_currency.upper(),
        separator=" ",
    ) 
    return text


ERROR_FETCHING_TEXT = "Something went wrong. Please try again later"

ERROR_NO_SUCH_CURRENCY = (
    "Unknown currency: {currency}, indicate real currency"
)


SET_MY_CURRENCY_HOW_TO = formatting.format_text(
    "Please, indicate your default currency, for example:",
    formatting.hcode("/set_my_currency RUB"),
)


SET_DEFAULT_CURRENCY_SUCCESS_MESSAGE = "You successfully set your currency: {currency}"