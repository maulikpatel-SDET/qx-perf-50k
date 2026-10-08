"""Service module 37888: business logic, no crypto."""


def calculate_total_37888(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37888():
    return 'module 37888 handles orders and invoices'
