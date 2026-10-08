"""Service module 610: business logic, no crypto."""


def calculate_total_610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_610():
    return 'module 610 handles orders and invoices'
