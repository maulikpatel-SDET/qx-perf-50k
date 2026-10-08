"""Service module 7429: business logic, no crypto."""


def calculate_total_7429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7429():
    return 'module 7429 handles orders and invoices'
