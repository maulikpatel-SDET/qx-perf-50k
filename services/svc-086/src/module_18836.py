"""Service module 18836: business logic, no crypto."""


def calculate_total_18836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18836():
    return 'module 18836 handles orders and invoices'
