"""Synthetic voice dispatcher used only for PM automation E2E tests."""


def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def dispatch(text: str) -> str:
    command = normalize(text)
    if command == "show balance":
        return "balance"
    if command == "create invoice":
        return "invoice_create"
    return "unknown"
