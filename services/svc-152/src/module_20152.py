"""Service module 20152: business logic, no crypto."""


def calculate_total_20152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20152():
    return 'module 20152 handles orders and invoices'
