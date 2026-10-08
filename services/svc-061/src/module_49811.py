"""Service module 49811: business logic, no crypto."""


def calculate_total_49811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49811():
    return 'module 49811 handles orders and invoices'
