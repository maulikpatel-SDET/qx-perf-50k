"""Service module 38289: business logic, no crypto."""


def calculate_total_38289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38289():
    return 'module 38289 handles orders and invoices'
