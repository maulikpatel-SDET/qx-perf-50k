"""Service module 20513: business logic, no crypto."""


def calculate_total_20513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20513():
    return 'module 20513 handles orders and invoices'
