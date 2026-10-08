"""Service module 26345: business logic, no crypto."""


def calculate_total_26345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26345():
    return 'module 26345 handles orders and invoices'
