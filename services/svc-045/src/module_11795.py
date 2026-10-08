"""Service module 11795: business logic, no crypto."""


def calculate_total_11795(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11795():
    return 'module 11795 handles orders and invoices'
