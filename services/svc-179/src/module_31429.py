"""Service module 31429: business logic, no crypto."""


def calculate_total_31429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31429():
    return 'module 31429 handles orders and invoices'
