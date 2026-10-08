"""Service module 3782: business logic, no crypto."""


def calculate_total_3782(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3782():
    return 'module 3782 handles orders and invoices'
