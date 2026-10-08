"""Service module 48280: business logic, no crypto."""


def calculate_total_48280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48280():
    return 'module 48280 handles orders and invoices'
