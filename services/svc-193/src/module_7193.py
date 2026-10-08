"""Service module 7193: business logic, no crypto."""


def calculate_total_7193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7193():
    return 'module 7193 handles orders and invoices'
