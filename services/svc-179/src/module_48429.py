"""Service module 48429: business logic, no crypto."""


def calculate_total_48429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48429():
    return 'module 48429 handles orders and invoices'
