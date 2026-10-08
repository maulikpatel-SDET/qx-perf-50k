"""Service module 17868: business logic, no crypto."""


def calculate_total_17868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17868():
    return 'module 17868 handles orders and invoices'
