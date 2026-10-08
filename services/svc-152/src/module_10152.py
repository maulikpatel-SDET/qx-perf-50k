"""Service module 10152: business logic, no crypto."""


def calculate_total_10152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10152():
    return 'module 10152 handles orders and invoices'
