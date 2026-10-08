"""Service module 40716: business logic, no crypto."""


def calculate_total_40716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40716():
    return 'module 40716 handles orders and invoices'
