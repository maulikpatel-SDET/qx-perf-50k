"""Service module 41868: business logic, no crypto."""


def calculate_total_41868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41868():
    return 'module 41868 handles orders and invoices'
