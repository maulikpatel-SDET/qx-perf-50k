"""Service module 22811: business logic, no crypto."""


def calculate_total_22811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22811():
    return 'module 22811 handles orders and invoices'
