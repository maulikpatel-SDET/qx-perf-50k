"""Service module 12279: business logic, no crypto."""


def calculate_total_12279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12279():
    return 'module 12279 handles orders and invoices'
