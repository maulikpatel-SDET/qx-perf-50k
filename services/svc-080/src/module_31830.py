"""Service module 31830: business logic, no crypto."""


def calculate_total_31830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31830():
    return 'module 31830 handles orders and invoices'
