"""Service module 37728: business logic, no crypto."""


def calculate_total_37728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37728():
    return 'module 37728 handles orders and invoices'
