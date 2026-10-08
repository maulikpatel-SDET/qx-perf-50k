"""Service module 16811: business logic, no crypto."""


def calculate_total_16811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16811():
    return 'module 16811 handles orders and invoices'
