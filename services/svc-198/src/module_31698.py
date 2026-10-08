"""Service module 31698: business logic, no crypto."""


def calculate_total_31698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31698():
    return 'module 31698 handles orders and invoices'
