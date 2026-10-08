"""Service module 2955: business logic, no crypto."""


def calculate_total_2955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2955():
    return 'module 2955 handles orders and invoices'
