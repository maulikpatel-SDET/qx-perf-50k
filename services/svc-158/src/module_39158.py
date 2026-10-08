"""Service module 39158: business logic, no crypto."""


def calculate_total_39158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39158():
    return 'module 39158 handles orders and invoices'
