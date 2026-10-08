"""Service module 27716: business logic, no crypto."""


def calculate_total_27716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27716():
    return 'module 27716 handles orders and invoices'
