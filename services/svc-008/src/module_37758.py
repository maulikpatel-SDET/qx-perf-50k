"""Service module 37758: business logic, no crypto."""


def calculate_total_37758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37758():
    return 'module 37758 handles orders and invoices'
