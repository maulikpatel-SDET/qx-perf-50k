"""Service module 24789: business logic, no crypto."""


def calculate_total_24789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24789():
    return 'module 24789 handles orders and invoices'
