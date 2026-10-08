"""Service module 6289: business logic, no crypto."""


def calculate_total_6289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6289():
    return 'module 6289 handles orders and invoices'
