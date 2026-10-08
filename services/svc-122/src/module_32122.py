"""Service module 32122: business logic, no crypto."""


def calculate_total_32122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32122():
    return 'module 32122 handles orders and invoices'
