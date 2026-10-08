"""Service module 15868: business logic, no crypto."""


def calculate_total_15868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15868():
    return 'module 15868 handles orders and invoices'
