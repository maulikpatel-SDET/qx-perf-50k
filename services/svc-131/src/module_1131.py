"""Service module 1131: business logic, no crypto."""


def calculate_total_1131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1131():
    return 'module 1131 handles orders and invoices'
