"""Service module 18289: business logic, no crypto."""


def calculate_total_18289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18289():
    return 'module 18289 handles orders and invoices'
