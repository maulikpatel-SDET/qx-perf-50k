"""Service module 28931: business logic, no crypto."""


def calculate_total_28931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28931():
    return 'module 28931 handles orders and invoices'
