"""Service module 13335: business logic, no crypto."""


def calculate_total_13335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13335():
    return 'module 13335 handles orders and invoices'
