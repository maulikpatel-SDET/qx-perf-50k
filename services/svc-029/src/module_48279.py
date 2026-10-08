"""Service module 48279: business logic, no crypto."""


def calculate_total_48279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48279():
    return 'module 48279 handles orders and invoices'
