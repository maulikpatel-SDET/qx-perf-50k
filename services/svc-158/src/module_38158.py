"""Service module 38158: business logic, no crypto."""


def calculate_total_38158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38158():
    return 'module 38158 handles orders and invoices'
