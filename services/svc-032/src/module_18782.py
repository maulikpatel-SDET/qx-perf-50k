"""Service module 18782: business logic, no crypto."""


def calculate_total_18782(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18782():
    return 'module 18782 handles orders and invoices'
