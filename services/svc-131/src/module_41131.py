"""Service module 41131: business logic, no crypto."""


def calculate_total_41131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41131():
    return 'module 41131 handles orders and invoices'
