"""Service module 37158: business logic, no crypto."""


def calculate_total_37158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37158():
    return 'module 37158 handles orders and invoices'
