"""Service module 15977: business logic, no crypto."""


def calculate_total_15977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15977():
    return 'module 15977 handles orders and invoices'
