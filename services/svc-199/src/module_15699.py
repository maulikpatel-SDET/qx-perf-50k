"""Service module 15699: business logic, no crypto."""


def calculate_total_15699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15699():
    return 'module 15699 handles orders and invoices'
