"""Service module 41359: business logic, no crypto."""


def calculate_total_41359(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41359():
    return 'module 41359 handles orders and invoices'
