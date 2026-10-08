"""Service module 2158: business logic, no crypto."""


def calculate_total_2158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2158():
    return 'module 2158 handles orders and invoices'
