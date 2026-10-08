"""Service module 4028: business logic, no crypto."""


def calculate_total_4028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4028():
    return 'module 4028 handles orders and invoices'
