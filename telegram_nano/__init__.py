import typing

from nano_api import (Object, DataField, ObjectField, IdField, ApiFunction, CachedStaticProperty, CachedProperty,
                      InputFile)


class WebhookInfo(Object):
    url = DataField(str)
    has_custom_certificate = DataField(bool)
    pending_update_count = DataField(int)

    last_error_date = DataField(int, optional=True)
    last_error_message = DataField(str, optional=True)
    max_connections = DataField(int, optional=True)
    allowed_updates = DataField(typing.List[str], optional=True)

    @staticmethod
    @ApiFunction(name='get_webhook_info')
    def get() -> 'WebhookInfo':
        pass

    @staticmethod
    @ApiFunction(name='delete_webhook')
    def delete() -> bool:
        pass

    @staticmethod
    @ApiFunction(name='set_webhook')
    def set(url: str, certificate: InputFile = None, max_connections: int = 40, allowed_updates: typing.List[str]=None):
        pass


class User(Object):
    id = IdField(int)
    is_bot = DataField(bool)
    first_name = DataField(str)
    last_name = DataField(str, optional=True)
    username = DataField(str, optional=True)
    language_code = DataField(str, optional=True)

    @CachedStaticProperty
    @ApiFunction(name='get_me')
    def me() -> 'User':
        pass

    @CachedProperty
    @ApiFunction(name='get_user_profile_photos')
    def profile_photos(user_id, offset: int = None, limit=100) -> 'UserProfilePhotos':
        pass


class MessageEntity(Object):
    type = DataField(str, one_of=('mention', 'hashtag', 'bot_command', 'url', 'email', 'bold', 'italic', 'code', 'pre',
                                  'text_link', 'text_mention'))
    offset = DataField(int)
    length = DataField(int)
    url = DataField(str, optional=True)
    user = ObjectField(User, optional=True)


class PhotoSize(Object):
    file_id = DataField(str)
    width = DataField(int)
    height = DataField(int)
    file_size = DataField(int, optional=True)


class Audio(Object):
    file_id = DataField(str)
    duration = DataField(int)
    performer = DataField(str, optional=True)
    title = DataField(str, optional=True)
    mime_Otype = DataField(str, optional=True)
    file_size = DataField(int, optional=True)


class Document(Object):
    file_id = DataField(str)
    thumb = ObjectField(PhotoSize, optional=True)
    file_name = DataField(str, optional=True)
    mime_Otype = DataField(str, optional=True)
    file_size = DataField(int, optional=True)


class Video(Object):
    file_id = DataField(str)
    width = DataField(int)
    height = DataField(int)
    duration = DataField(int)
    thumb = ObjectField(PhotoSize, optional=True)
    mime_Otype = DataField(str, optional=True)
    file_size = DataField(int, optional=True)


class Voice(Object):
    file_id = DataField(str)
    duration = DataField(int)
    mime_Otype = DataField(str, optional=True)
    file_size = DataField(int, optional=True)


class VideoNote(Object):
    file_id = DataField(str)
    length = DataField(int)
    duration = DataField(int)
    thumb = ObjectField(PhotoSize, optional=True)
    file_size = DataField(int, optional=True)


class Contact(Object):
    phone_number = DataField(str)
    first_name = DataField(str)
    last_name = DataField(str, optional=True)
    user_id = DataField(int, optional=True)


class Location(Object):
    longitude = DataField(float)
    latitude = DataField(float)


class Venue(Object):
    location = ObjectField(Location, optional=True)
    title = DataField(str)
    address = DataField(str)
    foursquare_id = DataField(str, optional=True)


class UserProfilePhotos(Object):
    total_count = DataField(int, optional=True)
    photos = ObjectField(typing.List[typing.List[PhotoSize]], optional=True)


class File(Object):
    file_id = IdField(str)
    file_size = DataField(int, optional=True)
    file_path = DataField(str, optional=True)

    def get_url(self, token):
        return "https://api.telegram.org/file/bot%s/%s" % (token, self.file_path)

    @staticmethod
    @ApiFunction(name='get_file')
    def by_id(file_id: str) -> 'File':
        pass


class ChatPhoto(Object):
    small_file_id = DataField(str)
    big_file_id = DataField(str)


class Chat(Object):
    id = IdField(int)
    type = DataField(str, one_of=('private', 'group', 'supergroup', 'channel'))
    title = DataField(str, optional=True)
    username = DataField(str, optional=True)
    first_name = DataField(str, optional=True)
    last_name = DataField(str, optional=True)
    all_members_are_administrators = DataField(bool, default=False)
    photo = ObjectField(ChatPhoto, optional=True)
    description = DataField(str, optional=True)
    invite_link = DataField(str, optional=True)
    pinned_message = ObjectField('Message', optional=True)

    @ApiFunction
    def send_message(chat_id, text: str, parse_mode: str = None, disable_web_page_preview=False,
                     disable_notification=False, reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def forward_message(chat_id, from_chat_id, message_id: int, disable_notification=False) -> 'Message':
        pass

    @ApiFunction
    def send_photo(chat_id, photo: typing.Union[str, InputFile], caption: str = '', disable_notification=False,
                   reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_audio(chat_id, audio: typing.Union[str, InputFile], caption: str = '', duration: int = None,
                   performer: str = None, title: str = None, disable_notification=False,
                   reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_document(chat_id, document: typing.Union[str, InputFile], caption: str = '', disable_notification=False,
                      reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_video(chat_id, video: typing.Union[str, InputFile], duration: int=None, width: int=None, height: int=None,
                   caption: str='', disable_notification=False, reply_to_message_id: int = None,
                   reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_voice(chat_id, voice: typing.Union[str, InputFile], caption: str='', duration: int=None,
                   disable_notification=False, reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_video_note(chat_id, video_note: typing.Union[str, InputFile], duration: int=None, length: int=None,
                        disable_notification=False, reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_location(chat_id, latitude: float, longitude: float, disable_notification=False,
                      reply_to_message_id: int=None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_venue(chat_id, latitude: float, longitude: float, title: str, address: str, foursquare_id: str,
                   disable_notification=False, reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_contact(chat_id, phone_number: str, first_name: str, last_name: str=None, disable_notification=False,
                     reply_to_message_id: int = None, reply_markup=None) -> 'Message':
        pass

    @ApiFunction
    def send_invoice(chat_id, title: str, description: str, payload: str, provider_token: str, start_parameter: str,
                     currency: str, prices: typing.List['LabeledPrice'], photo_url: str=None, photo_size: int=None,
                     photo_width: int=None, photo_height: int=None, need_name=False, need_phone_number=False,
                     need_email=False, need_shipping_address=False, is_flexible=False, disable_notification=False,
                     reply_to_message_id: int=None, reply_markup: 'InlineKeyboardMarkup'=None) -> 'Message':
        pass

    @ApiFunction
    def send_game(chat_id, game_short_name: str, disable_notification=False, reply_to_message_id: int=None,
                  reply_markup: 'InlineKeyboardMarkup'=None) -> 'Message':
        pass

    @ApiFunction
    def send_sticker(chat_id, sticker: typing.Union[str, InputFile], disable_notification=False, reply_to_message_id: int=None,
                     reply_markup: 'InlineKeyboardMarkup'=None) -> 'Message':
        pass

    @ApiFunction
    def send_chat_action(chat_id, action: str) -> bool:
        pass

    @ApiFunction(name='kick_chat_member')
    def kick_member(chat_id, user_id: int, until_date: int = None) -> bool:
        pass

    @ApiFunction(name='unban_chat_member')
    def unban_member(chat_id, user_id: int) -> bool:
        pass

    @ApiFunction(name='restrict_chat_member')
    def restrict_member(chat_id, user_id: int, until_date: int = None, can_send_messages=False,
                        can_send_media_messages=False, can_send_other_messages=False, can_add_web_page_previews=False
                        ) -> bool:
        pass

    @ApiFunction(name='promote_chat_member')
    def promote_member(chat_id, can_change_info=False, can_post_messages=False, can_edit_messages=False,
                       can_delete_messages=False, can_invite_users=False, can_restrict_members=False,
                       can_pin_messages=False, can_promote_members=False) -> bool:
        pass

    @ApiFunction(name='set_chat_photo')
    def set_photo(chat_id, photo: InputFile) -> bool:
        pass

    @ApiFunction(name='delete_chat_photo')
    def delete_photo(chat_id) -> bool:
        pass

    @ApiFunction(name='set_chat_title')
    def set_title(chat_id, title: str) -> bool:
        pass

    @ApiFunction(name='set_chat_description')
    def set_description(chat_id, description: str) -> bool:
        pass

    @ApiFunction(name='pin_chat_message')
    def pin_message(chat_id, message_id: int, disable_notification=False) -> bool:
        pass

    @ApiFunction(name='unpin_chat_message')
    def unpin_message(chat_id) -> bool:
        pass

    @ApiFunction(name='leave_chat')
    def leave(chat_id) -> bool:
        pass

    @staticmethod
    @ApiFunction(name='get_chat')
    def by_id(chat_id) -> 'Chat':
        pass

    @CachedProperty
    @ApiFunction(name='get_chat_administrators')
    def administrators(chat_id) -> typing.List['ChatMember']:
        pass

    @CachedProperty
    @ApiFunction(name='get_chat_members_count')
    def members_count(chat_id) -> int:
        pass

    @ApiFunction(name='get_chat_member')
    def get_member(chat_id, user_id: int) -> 'ChatMember':
        pass

    @ApiFunction(name='export_chat_invite_link')
    def export_invite_link(chat_id) -> str:
        pass


class Animation(Object):
    file_id = DataField(str)
    thumb = ObjectField(PhotoSize, optional=True)
    file_name = DataField(str, optional=True)
    mime_Otype = DataField(str, optional=True)
    file_size = DataField(int, optional=True)


class MaskPosition(Object):
    point = DataField(str, one_of=('forehead', 'eyes', 'mouth', 'chin'))
    x_shift = DataField(float)
    y_shift = DataField(float)
    scale = DataField(float)


class Sticker(Object):
    file_id = IdField(str)
    width = DataField(int)
    height = DataField(int)
    thumb = ObjectField(PhotoSize, optional=True)
    emoji = DataField(str, optional=True)
    set_name = DataField(str, optional=True)
    mask_position = ObjectField(MaskPosition, optional=True)
    file_size = DataField(int, optional=True)

    @ApiFunction(name='set_sticker_position_in_set')
    def set_position(sticker, position: int) -> bool:
        pass

    @ApiFunction(name='delete_sticker_from_set')
    def delete(sticker) -> bool:
        pass


class StickerSet(Object):
    name = IdField(str)
    title = DataField(str)
    contains_masks = DataField(bool)
    stickers = ObjectField(typing.List[Sticker])

    @staticmethod
    @ApiFunction(name='get_sticker_set')
    def by_name(name: str) -> 'StickerSet':
        pass

    @staticmethod
    @ApiFunction(name='create_new_sticker_set')
    def create(user_id: int, name: str, title: str, png_sticker: typing.Union[str, InputFile], emojis: str,
               contains_masks=False, mask_position: MaskPosition=None) -> bool:
        pass

    @staticmethod
    @ApiFunction(name='upload_sticker_file')
    def upload(user_id: int, png_sticker: InputFile) -> File:
        pass

    @ApiFunction(name='add_sticker_to_set')
    def add_sticker(name, user_id: int, png_sticker: typing.Union[str, InputFile], emojis: str,
                    mask_position: MaskPosition=None) -> bool:
        pass


class Game(Object):
    description = DataField(str)
    title = DataField(str)
    photo = ObjectField(typing.List[PhotoSize])
    text = DataField(str, optional=True)
    text_entities = ObjectField(typing.List[MessageEntity], optional=True)
    animation = ObjectField(Animation, optional=True)


class Invoice(Object):
    title = DataField(str)
    description = DataField(str)
    start_parameter = DataField(str)
    currency = DataField(str)
    total_amount = DataField(int)


class ShippingAddress(Object):
    country_code = DataField(str)
    state = DataField(str)
    city = DataField(str)
    street_line1 = DataField(str)
    street_line2 = DataField(str)
    post_code = DataField(str)


class OrderInfo(Object):
    name = DataField(str, optional=True)
    phone_number = DataField(str, optional=True)
    email = DataField(str, optional=True)
    shipping_address = ObjectField(ShippingAddress, optional=True)


class SuccessfulPayment(Object):
    currency = DataField(str)
    total_amount = DataField(int)
    invoice_payload = DataField(str)
    shipping_option_id = DataField(str, optional=True)
    order_info = ObjectField(OrderInfo, optional=True)
    provider_payment_charge_id = DataField(str)
    telegram_payment_charge_id = DataField(str)


class Message(Object):
    message_id = IdField(int)
    from_ = ObjectField(User, real_name='from')
    date = DataField(int)
    chat = ObjectField(Chat)

    forward_from = ObjectField(User, optional=True)
    forward_from_chat = ObjectField(Chat, optional=True)
    forward_from_message_id = DataField(int, optional=True)
    forward_signature = DataField(str, optional=True)
    forward_date = DataField(int, optional=True)

    reply_to_message = ObjectField('Message', optional=True)
    edit_date = DataField(int, optional=True)
    author_signature = DataField(str, optional=True)
    text = DataField(str, optional=True)
    entities = ObjectField(typing.List[MessageEntity], optional=True)

    caption = DataField(str, optional=True)
    audio = ObjectField(Audio, optional=True)
    document = ObjectField(Document, optional=True)
    game = ObjectField(Game, optional=True)
    photo = ObjectField(typing.List[PhotoSize], optional=True)
    sticker = ObjectField(Sticker, optional=True)
    voice = ObjectField(Voice, optional=True)
    video = ObjectField(Video, optional=True)
    video_note = ObjectField(VideoNote, optional=True)
    contact = ObjectField(Contact, optional=True)
    location = ObjectField(Location, optional=True)
    venue = ObjectField(Venue, optional=True)
    invoice = ObjectField(Invoice, optional=True)
    successful_payment = ObjectField(SuccessfulPayment, optional=True)

    new_chat_members = ObjectField(typing.List[User], optional=True)
    new_chat_member = ObjectField(User, optional=True)
    left_chat_member = ObjectField(User, optional=True)

    new_chat_Otitle = DataField(str, optional=True)
    new_chat_photo = ObjectField(typing.List[PhotoSize], optional=True)
    delete_chat_photo = DataField(bool, default=False)

    group_chat_created = DataField(bool, default=False)
    supergroup_chat_created = DataField(bool, default=False)
    channel_chat_created = DataField(bool, default=False)
    migrate_Oto_chat_id = DataField(int, optional=True)
    migrate_from_chat_id = DataField(int, optional=True)

    pinned_message = DataField(int, optional=True)

    @ApiFunction(name='edit_message_text')
    def edit_text(message_id, text: str, chat_id: typing.Union[int, str]=None, parse_mode: str=None,
                          disable_web_page_preview=False, reply_markup: 'InlineKeyboardMarkup'=None) -> 'Message':
        yield 'append', dict(chat_id=message_id.chat.id)

    @ApiFunction(name='edit_message_caption')
    def edit_caption(message_id, caption: str = None, reply_markup: 'InlineKeyboardMarkup'=None) -> 'Message':
        yield 'append', dict(chat_id=message_id.chat.id)

    @ApiFunction(name='edit_message_reply_markup')
    def edit_reply_markup(message_id, reply_markup: 'InlineKeyboardMarkup'=None) -> 'Message':
        yield 'append', dict(chat_id=message_id.chat.id)

    @ApiFunction(name='delete_message')
    def delete_message(message_id) -> bool:
        yield 'append', dict(chat_id=message_id.chat.id)

    @ApiFunction
    def set_game_score(message_id, user_id: int, score: int, force=False, disable_edit_message=False) -> bool:
        yield 'append', dict(chat_id=message_id.chat.id)

    @ApiFunction
    def get_game_high_scores(message_id, user_id: int) -> typing.List['GameHighScore']:
        yield 'append', dict(chat_id=message_id.chat.id)


class KeyboardButton(Object):
    text = DataField(str)
    request_contact = DataField(bool, default=False)
    request_location = DataField(bool, default=False)


class ReplyKeyboardMarkup(Object):
    keyboard = ObjectField(typing.List[typing.List[KeyboardButton]])
    resize_keyboard = DataField(bool, default=False)
    one_Otime_keyboard = DataField(bool, default=False)
    selective = DataField(bool, default=False)


class ReplyKeyboardRemove(Object):
    selective = DataField(bool, default=False)


class CallbackGame(Object):
    pass


class InlineKeyboardButton(Object):
    text = DataField(str)
    url = DataField(str, optional=True)
    callback_data = DataField(str, optional=True)
    switch_inline_query = DataField(str, optional=True)
    switch_inline_query_current_chat = DataField(str, optional=True)
    callback_game = ObjectField(CallbackGame, optional=True)
    pay = DataField(bool, default=False)


class InlineKeyboardMarkup(Object):
    keyboard = ObjectField(typing.List[typing.List[InlineKeyboardButton]])


class CallbackQuery(Object):
    id = IdField(str)
    from_ = ObjectField(User, real_name='from')
    message = ObjectField(Message, optional=True)
    inline_message_id = DataField(str, optional=True)
    chat_instance = DataField(str, optional=True)
    data = DataField(str, optional=True)
    game_short_name = DataField(str, optional=True)

    @ApiFunction(name='answer_callback_query')
    def answer(callback_query_id, text: str=None, show_alert=False, url: str=None, cache_time=0) -> bool:
        pass


class ForceReply(Object):
    selective = DataField(bool, default=False)


class ChatMember(Object):
    user = ObjectField(User)
    status = DataField(str, one_of=('creator', 'administrator', 'member', 'restricted', 'left', 'kicked'))
    until_date = DataField(int, optional=True)


class ResponseParameters(Object):
    migrate_Oto_chat_id = DataField(int, optional=True)
    retry_after = DataField(int, optional=True)

    can_be_edited = DataField(bool, default=False)
    can_change_info = DataField(bool, default=False)
    can_post_messages = DataField(bool, default=False)
    can_edit_messages = DataField(bool, default=False)
    can_delete_messages = DataField(bool, default=False)
    can_invite_users = DataField(bool, default=False)
    can_restrict_members = DataField(bool, default=False)
    can_pin_messages = DataField(bool, default=False)
    can_promote_members = DataField(bool, default=False)
    can_send_messages = DataField(bool, default=False)
    can_send_media_messages = DataField(bool, default=False)
    can_send_other_messages = DataField(bool, default=False)
    can_add_web_page_previews = DataField(bool, default=False)


class InlineQuery(Object):
    id = IdField(str)
    from_ = ObjectField(User, real_name='from')
    location = ObjectField(Location, optional=True)
    query = DataField(str)
    offset = DataField(str)

    @ApiFunction(name='answer_inline_query')
    def answer(inline_query_id, results: typing.List['InlineQueryResult'], cache_time=300, is_personal=False,
               next_offset: str=None, switch_pm_text: str=None, switch_pm_parameter: str=None) -> bool:
        pass


class ChosenInlineResult(Object):
    result_id = IdField(str)
    from_ = ObjectField(User, real_name='from')
    location = ObjectField(Location, optional=True)
    inline_message_id = DataField(str, optional=True)
    query = DataField(str)

    @ApiFunction(name='edit_message_text')
    def edit_text(self, text: str, parse_mode: str = None, disable_web_page_preview=False,
                  reply_markup: InlineKeyboardMarkup = None) -> Message:
        yield 'append', dict(self=None, inline_message_id=self.inline_message_id)

    @ApiFunction(name='edit_message_caption')
    def edit_caption(self, caption: str = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
        yield 'append', dict(self=None, inline_message_id=self.inline_message_id)

    @ApiFunction(name='edit_message_reply_markup')
    def edit_reply_markup(self, reply_markup: InlineKeyboardMarkup = None) -> Message:
        yield 'append', dict(self=None, inline_message_id=self.inline_message_id)

    @ApiFunction
    def get_game_high_scores(self) -> typing.List['GameHighScore']:
        yield 'append', dict(self=None, inline_message_id=self.inline_message_id)

    @ApiFunction
    def set_game_score(self, user_id: int, score: int, force=False, disable_edit_message=False) -> bool:
        yield 'append', dict(self=None, inline_message_id=self.inline_message_id)


class LabeledPrice(Object):
    label = DataField(str)
    amount = DataField(int)


class ShippingOption(Object):
    id = IdField(str)
    title = DataField(str)
    prices = ObjectField(typing.List[LabeledPrice])


class ShippingQuery(Object):
    id = IdField(str)
    from_ = ObjectField(User, real_name='from')
    invoice_payload = DataField(str)
    shipping_address = ObjectField(ShippingAddress)

    @ApiFunction(name='answer_shipping_query')
    def answer(shipping_query_id, ok: bool, shipping_options: typing.List[ShippingOption]=None, error_message: str=None
               ) -> bool:
        pass


class PreCheckoutQuery(Object):
    id = IdField(str)
    from_ = ObjectField(User, real_name='from')
    currency = DataField(str)
    total_amount = DataField(int)
    invoice_payload = DataField(str)
    shipping_option_id = DataField(str, optional=True)
    order_info = ObjectField(OrderInfo, optional=True)

    @ApiFunction(name='answer_pre_checkout_query')
    def answer(pre_checkout_query_id, ok: bool, error_message: str=None) -> bool:
        pass


class Update(Object):
    update_id = IdField(int)
    message = ObjectField(Message, optional=True)
    edited_message = ObjectField(Message, optional=True)
    channel_post = ObjectField(Message, optional=True)
    edited_channel_post = ObjectField(Message, optional=True)
    inline_query = ObjectField(InlineQuery, optional=True)
    chosen_inline_result = ObjectField(ChosenInlineResult, optional=True)
    callback_query = ObjectField(ShippingQuery, optional=True)
    pre_checkout_query = ObjectField(PreCheckoutQuery, optional=True)

    @staticmethod
    @ApiFunction(name='get_updates')
    def pool(offset: int=None, limit: int=100, timeout: int=0, allowed_updates: typing.List[str]=None
                    ) -> typing.List['Update']:
        pass


class GameHighScore(Object):
    position = DataField(int)
    user = ObjectField(User)
    score = DataField(int)
