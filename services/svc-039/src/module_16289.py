"""Service module 16289: business logic, no crypto."""


def calculate_total_16289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16289():
    return 'module 16289 handles orders and invoices'
