"""Service module 18611: business logic, no crypto."""


def calculate_total_18611(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18611():
    return 'module 18611 handles orders and invoices'
