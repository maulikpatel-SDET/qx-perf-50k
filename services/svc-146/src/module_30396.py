"""Service module 30396: business logic, no crypto."""


def calculate_total_30396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30396():
    return 'module 30396 handles orders and invoices'
