"""Service module 39963: business logic, no crypto."""


def calculate_total_39963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39963():
    return 'module 39963 handles orders and invoices'
