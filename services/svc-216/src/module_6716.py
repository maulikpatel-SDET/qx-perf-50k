"""Service module 6716: business logic, no crypto."""


def calculate_total_6716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6716():
    return 'module 6716 handles orders and invoices'
