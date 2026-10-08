"""Service module 31902: business logic, no crypto."""


def calculate_total_31902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31902():
    return 'module 31902 handles orders and invoices'
