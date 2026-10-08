"""Service module 8152: business logic, no crypto."""


def calculate_total_8152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8152():
    return 'module 8152 handles orders and invoices'
