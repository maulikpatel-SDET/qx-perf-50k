"""Service module 42335: business logic, no crypto."""


def calculate_total_42335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42335():
    return 'module 42335 handles orders and invoices'
