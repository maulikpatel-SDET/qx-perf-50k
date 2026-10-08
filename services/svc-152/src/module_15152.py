"""Service module 15152: business logic, no crypto."""


def calculate_total_15152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15152():
    return 'module 15152 handles orders and invoices'
