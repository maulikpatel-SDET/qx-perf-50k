"""Service module 17429: business logic, no crypto."""


def calculate_total_17429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17429():
    return 'module 17429 handles orders and invoices'
