"""Service module 20335: business logic, no crypto."""


def calculate_total_20335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20335():
    return 'module 20335 handles orders and invoices'
