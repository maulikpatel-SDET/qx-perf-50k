"""Service module 30789: business logic, no crypto."""


def calculate_total_30789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30789():
    return 'module 30789 handles orders and invoices'
