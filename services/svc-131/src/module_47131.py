"""Service module 47131: business logic, no crypto."""


def calculate_total_47131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47131():
    return 'module 47131 handles orders and invoices'
