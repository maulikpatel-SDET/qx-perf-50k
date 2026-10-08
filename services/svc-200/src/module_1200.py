"""Service module 1200: business logic, no crypto."""


def calculate_total_1200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1200():
    return 'module 1200 handles orders and invoices'
