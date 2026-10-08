"""Service module 11902: business logic, no crypto."""


def calculate_total_11902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11902():
    return 'module 11902 handles orders and invoices'
