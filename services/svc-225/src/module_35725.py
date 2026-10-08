"""Service module 35725: business logic, no crypto."""


def calculate_total_35725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35725():
    return 'module 35725 handles orders and invoices'
