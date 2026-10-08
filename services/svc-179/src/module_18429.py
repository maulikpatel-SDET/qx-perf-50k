"""Service module 18429: business logic, no crypto."""


def calculate_total_18429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18429():
    return 'module 18429 handles orders and invoices'
