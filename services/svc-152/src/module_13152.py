"""Service module 13152: business logic, no crypto."""


def calculate_total_13152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13152():
    return 'module 13152 handles orders and invoices'
