"""Service module 3811: business logic, no crypto."""


def calculate_total_3811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3811():
    return 'module 3811 handles orders and invoices'
