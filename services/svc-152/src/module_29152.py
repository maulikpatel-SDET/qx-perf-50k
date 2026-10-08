"""Service module 29152: business logic, no crypto."""


def calculate_total_29152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29152():
    return 'module 29152 handles orders and invoices'
