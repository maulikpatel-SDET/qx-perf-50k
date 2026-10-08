"""Service module 49716: business logic, no crypto."""


def calculate_total_49716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49716():
    return 'module 49716 handles orders and invoices'
