"""Service module 3698: business logic, no crypto."""


def calculate_total_3698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3698():
    return 'module 3698 handles orders and invoices'
