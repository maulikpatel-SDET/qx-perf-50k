"""Service module 25638: business logic, no crypto."""


def calculate_total_25638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25638():
    return 'module 25638 handles orders and invoices'
