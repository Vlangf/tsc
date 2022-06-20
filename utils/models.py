from dataclasses import dataclass
from typing import List


@dataclass
class WebhookInfoResult:
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: str
    last_error_date: int
    last_error_message: str
    max_connections: int
    allowed_updates: List[str]


@dataclass
class WebhookInfo:
    ok: bool
    result: WebhookInfoResult


@dataclass
class WebhookSetOrDelete:
    ok: bool
    error_code: int
    description: str


@dataclass
class From:
    id: int
    is_bot: bool
    first_name: str
    username: str
    language_code: str


@dataclass
class Chat:
    id: int
    first_name: str
    username: str
    type: str


@dataclass
class Message:
    message_id: int
    from_: From
    chat: Chat
    date: int
    text: str


@dataclass
class UpdateResult:
    update_id: int
    message: Message


@dataclass
class Update:
    ok: bool
    result: List[UpdateResult]
