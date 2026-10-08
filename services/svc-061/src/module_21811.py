"""Service module 21811: business logic, no crypto."""


def calculate_total_21811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21811():
    return 'module 21811 handles orders and invoices'
