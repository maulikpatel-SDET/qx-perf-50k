"""Service module 8151: business logic, no crypto."""


def calculate_total_8151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8151():
    return 'module 8151 handles orders and invoices'
