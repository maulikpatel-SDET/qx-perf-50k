"""Service module 3105: business logic, no crypto."""


def calculate_total_3105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3105():
    return 'module 3105 handles orders and invoices'
