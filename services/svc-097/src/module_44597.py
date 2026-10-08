"""Service module 44597: business logic, no crypto."""


def calculate_total_44597(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44597():
    return 'module 44597 handles orders and invoices'
