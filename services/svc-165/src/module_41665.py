"""Service module 41665: business logic, no crypto."""


def calculate_total_41665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41665():
    return 'module 41665 handles orders and invoices'
