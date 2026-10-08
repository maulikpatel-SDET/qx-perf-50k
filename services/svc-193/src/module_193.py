"""Service module 193: business logic, no crypto."""


def calculate_total_193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_193():
    return 'module 193 handles orders and invoices'
