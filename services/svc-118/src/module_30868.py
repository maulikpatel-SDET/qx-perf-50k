"""Service module 30868: business logic, no crypto."""


def calculate_total_30868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30868():
    return 'module 30868 handles orders and invoices'
