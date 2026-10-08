"""Service module 35152: business logic, no crypto."""


def calculate_total_35152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35152():
    return 'module 35152 handles orders and invoices'
