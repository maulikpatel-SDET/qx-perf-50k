"""Service module 4795: business logic, no crypto."""


def calculate_total_4795(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4795():
    return 'module 4795 handles orders and invoices'
