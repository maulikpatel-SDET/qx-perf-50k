"""Service module 47802: business logic, no crypto."""


def calculate_total_47802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47802():
    return 'module 47802 handles orders and invoices'
