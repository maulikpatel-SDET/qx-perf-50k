"""Service module 279: business logic, no crypto."""


def calculate_total_279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_279():
    return 'module 279 handles orders and invoices'
