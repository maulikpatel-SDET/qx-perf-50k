"""Service module 29517: business logic, no crypto."""


def calculate_total_29517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29517():
    return 'module 29517 handles orders and invoices'
