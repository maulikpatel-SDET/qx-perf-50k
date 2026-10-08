"""Service module 17811: business logic, no crypto."""


def calculate_total_17811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17811():
    return 'module 17811 handles orders and invoices'
