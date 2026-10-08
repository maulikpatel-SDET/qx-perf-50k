"""Service module 11789: business logic, no crypto."""


def calculate_total_11789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11789():
    return 'module 11789 handles orders and invoices'
