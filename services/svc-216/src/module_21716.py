"""Service module 21716: business logic, no crypto."""


def calculate_total_21716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21716():
    return 'module 21716 handles orders and invoices'
