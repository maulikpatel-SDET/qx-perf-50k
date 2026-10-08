"""Service module 14816: business logic, no crypto."""


def calculate_total_14816(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14816():
    return 'module 14816 handles orders and invoices'
