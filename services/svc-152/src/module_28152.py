"""Service module 28152: business logic, no crypto."""


def calculate_total_28152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28152():
    return 'module 28152 handles orders and invoices'
