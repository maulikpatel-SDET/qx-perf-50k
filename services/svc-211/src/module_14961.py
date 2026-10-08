"""Service module 14961: business logic, no crypto."""


def calculate_total_14961(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14961():
    return 'module 14961 handles orders and invoices'
