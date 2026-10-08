"""Service module 45143: business logic, no crypto."""


def calculate_total_45143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45143():
    return 'module 45143 handles orders and invoices'
