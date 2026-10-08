"""Service module 33876: business logic, no crypto."""


def calculate_total_33876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33876():
    return 'module 33876 handles orders and invoices'
