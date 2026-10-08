"""Service module 15950: business logic, no crypto."""


def calculate_total_15950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15950():
    return 'module 15950 handles orders and invoices'
