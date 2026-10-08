"""Service module 49795: business logic, no crypto."""


def calculate_total_49795(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49795():
    return 'module 49795 handles orders and invoices'
