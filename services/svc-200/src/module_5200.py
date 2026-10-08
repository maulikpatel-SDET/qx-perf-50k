"""Service module 5200: business logic, no crypto."""


def calculate_total_5200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5200():
    return 'module 5200 handles orders and invoices'
