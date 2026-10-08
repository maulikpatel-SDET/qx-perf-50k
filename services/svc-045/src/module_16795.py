"""Service module 16795: business logic, no crypto."""


def calculate_total_16795(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16795():
    return 'module 16795 handles orders and invoices'
