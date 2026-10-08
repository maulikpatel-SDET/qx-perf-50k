"""Service module 597: business logic, no crypto."""


def calculate_total_597(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_597():
    return 'module 597 handles orders and invoices'
