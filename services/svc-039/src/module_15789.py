"""Service module 15789: business logic, no crypto."""


def calculate_total_15789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15789():
    return 'module 15789 handles orders and invoices'
