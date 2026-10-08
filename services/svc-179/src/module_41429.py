"""Service module 41429: business logic, no crypto."""


def calculate_total_41429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41429():
    return 'module 41429 handles orders and invoices'
