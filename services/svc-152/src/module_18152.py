"""Service module 18152: business logic, no crypto."""


def calculate_total_18152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18152():
    return 'module 18152 handles orders and invoices'
