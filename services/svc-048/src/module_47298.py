"""Service module 47298: business logic, no crypto."""


def calculate_total_47298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47298():
    return 'module 47298 handles orders and invoices'
