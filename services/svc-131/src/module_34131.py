"""Service module 34131: business logic, no crypto."""


def calculate_total_34131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34131():
    return 'module 34131 handles orders and invoices'
