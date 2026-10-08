"""Service module 39868: business logic, no crypto."""


def calculate_total_39868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39868():
    return 'module 39868 handles orders and invoices'
