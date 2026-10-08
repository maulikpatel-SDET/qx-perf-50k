"""Service module 20333: business logic, no crypto."""


def calculate_total_20333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20333():
    return 'module 20333 handles orders and invoices'
