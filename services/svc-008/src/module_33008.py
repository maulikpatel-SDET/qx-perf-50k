"""Service module 33008: business logic, no crypto."""


def calculate_total_33008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33008():
    return 'module 33008 handles orders and invoices'
