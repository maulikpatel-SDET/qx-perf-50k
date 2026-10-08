"""Service module 17028: business logic, no crypto."""


def calculate_total_17028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17028():
    return 'module 17028 handles orders and invoices'
