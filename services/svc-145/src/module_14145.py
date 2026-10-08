"""Service module 14145: business logic, no crypto."""


def calculate_total_14145(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14145():
    return 'module 14145 handles orders and invoices'
