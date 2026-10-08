"""Service module 48725: business logic, no crypto."""


def calculate_total_48725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48725():
    return 'module 48725 handles orders and invoices'
