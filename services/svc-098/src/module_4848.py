"""Service module 4848: business logic, no crypto."""


def calculate_total_4848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4848():
    return 'module 4848 handles orders and invoices'
