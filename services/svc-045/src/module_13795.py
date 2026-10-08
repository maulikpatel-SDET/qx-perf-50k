"""Service module 13795: business logic, no crypto."""


def calculate_total_13795(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13795():
    return 'module 13795 handles orders and invoices'
