"""Service module 12416: business logic, no crypto."""


def calculate_total_12416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12416():
    return 'module 12416 handles orders and invoices'
