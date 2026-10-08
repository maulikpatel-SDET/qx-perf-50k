"""Service module 24158: business logic, no crypto."""


def calculate_total_24158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24158():
    return 'module 24158 handles orders and invoices'
