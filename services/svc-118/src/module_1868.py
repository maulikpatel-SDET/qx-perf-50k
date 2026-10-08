"""Service module 1868: business logic, no crypto."""


def calculate_total_1868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1868():
    return 'module 1868 handles orders and invoices'
