"""Service module 38800: business logic, no crypto."""


def calculate_total_38800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38800():
    return 'module 38800 handles orders and invoices'
