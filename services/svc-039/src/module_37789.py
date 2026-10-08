"""Service module 37789: business logic, no crypto."""


def calculate_total_37789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37789():
    return 'module 37789 handles orders and invoices'
