"""Service module 29811: business logic, no crypto."""


def calculate_total_29811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29811():
    return 'module 29811 handles orders and invoices'
