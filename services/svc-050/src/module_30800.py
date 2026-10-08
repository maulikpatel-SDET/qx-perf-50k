"""Service module 30800: business logic, no crypto."""


def calculate_total_30800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30800():
    return 'module 30800 handles orders and invoices'
