"""Service module 28416: business logic, no crypto."""


def calculate_total_28416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28416():
    return 'module 28416 handles orders and invoices'
