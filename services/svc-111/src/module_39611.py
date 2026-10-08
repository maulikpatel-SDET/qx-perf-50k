"""Service module 39611: business logic, no crypto."""


def calculate_total_39611(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39611():
    return 'module 39611 handles orders and invoices'
