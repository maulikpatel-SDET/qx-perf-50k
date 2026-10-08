"""Service module 36611: business logic, no crypto."""


def calculate_total_36611(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36611():
    return 'module 36611 handles orders and invoices'
