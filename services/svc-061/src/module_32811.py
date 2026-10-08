"""Service module 32811: business logic, no crypto."""


def calculate_total_32811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32811():
    return 'module 32811 handles orders and invoices'
