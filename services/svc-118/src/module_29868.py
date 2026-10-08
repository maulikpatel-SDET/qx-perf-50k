"""Service module 29868: business logic, no crypto."""


def calculate_total_29868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29868():
    return 'module 29868 handles orders and invoices'
