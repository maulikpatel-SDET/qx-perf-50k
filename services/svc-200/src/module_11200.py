"""Service module 11200: business logic, no crypto."""


def calculate_total_11200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11200():
    return 'module 11200 handles orders and invoices'
