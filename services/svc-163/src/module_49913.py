"""Service module 49913: business logic, no crypto."""


def calculate_total_49913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49913():
    return 'module 49913 handles orders and invoices'
