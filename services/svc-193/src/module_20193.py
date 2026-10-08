"""Service module 20193: business logic, no crypto."""


def calculate_total_20193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20193():
    return 'module 20193 handles orders and invoices'
