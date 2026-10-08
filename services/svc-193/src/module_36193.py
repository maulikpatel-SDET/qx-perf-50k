"""Service module 36193: business logic, no crypto."""


def calculate_total_36193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36193():
    return 'module 36193 handles orders and invoices'
