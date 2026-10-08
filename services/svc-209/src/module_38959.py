"""Service module 38959: business logic, no crypto."""


def calculate_total_38959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38959():
    return 'module 38959 handles orders and invoices'
