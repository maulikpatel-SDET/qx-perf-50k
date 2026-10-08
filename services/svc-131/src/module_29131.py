"""Service module 29131: business logic, no crypto."""


def calculate_total_29131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29131():
    return 'module 29131 handles orders and invoices'
