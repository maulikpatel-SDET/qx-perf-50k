"""Service module 15289: business logic, no crypto."""


def calculate_total_15289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15289():
    return 'module 15289 handles orders and invoices'
