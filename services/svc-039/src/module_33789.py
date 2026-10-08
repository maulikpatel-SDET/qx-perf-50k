"""Service module 33789: business logic, no crypto."""


def calculate_total_33789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33789():
    return 'module 33789 handles orders and invoices'
