"""Service module 36131: business logic, no crypto."""


def calculate_total_36131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36131():
    return 'module 36131 handles orders and invoices'
