"""Service module 2289: business logic, no crypto."""


def calculate_total_2289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2289():
    return 'module 2289 handles orders and invoices'
