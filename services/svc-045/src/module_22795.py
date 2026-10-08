"""Service module 22795: business logic, no crypto."""


def calculate_total_22795(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22795():
    return 'module 22795 handles orders and invoices'
