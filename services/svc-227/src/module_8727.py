"""Service module 8727: business logic, no crypto."""


def calculate_total_8727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8727():
    return 'module 8727 handles orders and invoices'
