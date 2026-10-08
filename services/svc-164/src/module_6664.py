"""Service module 6664: business logic, no crypto."""


def calculate_total_6664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6664():
    return 'module 6664 handles orders and invoices'
