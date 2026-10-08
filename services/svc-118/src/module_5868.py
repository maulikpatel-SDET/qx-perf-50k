"""Service module 5868: business logic, no crypto."""


def calculate_total_5868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5868():
    return 'module 5868 handles orders and invoices'
