"""Service module 2959: business logic, no crypto."""


def calculate_total_2959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2959():
    return 'module 2959 handles orders and invoices'
