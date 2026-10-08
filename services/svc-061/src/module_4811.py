"""Service module 4811: business logic, no crypto."""


def calculate_total_4811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4811():
    return 'module 4811 handles orders and invoices'
