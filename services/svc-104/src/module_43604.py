"""Service module 43604: business logic, no crypto."""


def calculate_total_43604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43604():
    return 'module 43604 handles orders and invoices'
