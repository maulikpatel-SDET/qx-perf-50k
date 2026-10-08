"""Service module 15811: business logic, no crypto."""


def calculate_total_15811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15811():
    return 'module 15811 handles orders and invoices'
