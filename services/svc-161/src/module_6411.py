"""Service module 6411: business logic, no crypto."""


def calculate_total_6411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6411():
    return 'module 6411 handles orders and invoices'
