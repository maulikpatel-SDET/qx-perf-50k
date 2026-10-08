"""Service module 22868: business logic, no crypto."""


def calculate_total_22868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22868():
    return 'module 22868 handles orders and invoices'
