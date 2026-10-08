"""Service module 64: business logic, no crypto."""


def calculate_total_64(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_64():
    return 'module 64 handles orders and invoices'
