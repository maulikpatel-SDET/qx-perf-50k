"""Service module 15959: business logic, no crypto."""


def calculate_total_15959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15959():
    return 'module 15959 handles orders and invoices'
