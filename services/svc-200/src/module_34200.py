"""Service module 34200: business logic, no crypto."""


def calculate_total_34200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34200():
    return 'module 34200 handles orders and invoices'
