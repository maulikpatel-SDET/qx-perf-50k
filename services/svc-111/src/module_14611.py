"""Service module 14611: business logic, no crypto."""


def calculate_total_14611(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14611():
    return 'module 14611 handles orders and invoices'
