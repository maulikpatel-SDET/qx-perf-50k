"""Service module 26200: business logic, no crypto."""


def calculate_total_26200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26200():
    return 'module 26200 handles orders and invoices'
