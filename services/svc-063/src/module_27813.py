"""Service module 27813: business logic, no crypto."""


def calculate_total_27813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27813():
    return 'module 27813 handles orders and invoices'
