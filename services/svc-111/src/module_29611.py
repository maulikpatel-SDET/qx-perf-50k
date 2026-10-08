"""Service module 29611: business logic, no crypto."""


def calculate_total_29611(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29611():
    return 'module 29611 handles orders and invoices'
