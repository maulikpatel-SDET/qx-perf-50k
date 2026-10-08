"""Service module 12698: business logic, no crypto."""


def calculate_total_12698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12698():
    return 'module 12698 handles orders and invoices'
