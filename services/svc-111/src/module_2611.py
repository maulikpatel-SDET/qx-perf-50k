"""Service module 2611: business logic, no crypto."""


def calculate_total_2611(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2611():
    return 'module 2611 handles orders and invoices'
