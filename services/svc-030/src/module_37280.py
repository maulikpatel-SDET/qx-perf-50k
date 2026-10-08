"""Service module 37280: business logic, no crypto."""


def calculate_total_37280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37280():
    return 'module 37280 handles orders and invoices'
