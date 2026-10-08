"""Service module 28789: business logic, no crypto."""


def calculate_total_28789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28789():
    return 'module 28789 handles orders and invoices'
