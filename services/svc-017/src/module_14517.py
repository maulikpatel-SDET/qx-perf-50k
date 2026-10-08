"""Service module 14517: business logic, no crypto."""


def calculate_total_14517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14517():
    return 'module 14517 handles orders and invoices'
