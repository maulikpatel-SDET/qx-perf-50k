"""Service module 16712: business logic, no crypto."""


def calculate_total_16712(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16712():
    return 'module 16712 handles orders and invoices'
