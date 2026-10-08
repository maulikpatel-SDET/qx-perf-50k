"""Service module 30611: business logic, no crypto."""


def calculate_total_30611(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30611():
    return 'module 30611 handles orders and invoices'
