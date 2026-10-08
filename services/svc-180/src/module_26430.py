"""Service module 26430: business logic, no crypto."""


def calculate_total_26430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26430():
    return 'module 26430 handles orders and invoices'
