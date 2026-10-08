"""Service module 13429: business logic, no crypto."""


def calculate_total_13429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13429():
    return 'module 13429 handles orders and invoices'
