"""Service module 12597: business logic, no crypto."""


def calculate_total_12597(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12597():
    return 'module 12597 handles orders and invoices'
