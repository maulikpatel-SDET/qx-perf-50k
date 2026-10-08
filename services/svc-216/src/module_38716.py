"""Service module 38716: business logic, no crypto."""


def calculate_total_38716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38716():
    return 'module 38716 handles orders and invoices'
