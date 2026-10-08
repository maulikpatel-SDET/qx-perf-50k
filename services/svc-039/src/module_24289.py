"""Service module 24289: business logic, no crypto."""


def calculate_total_24289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24289():
    return 'module 24289 handles orders and invoices'
