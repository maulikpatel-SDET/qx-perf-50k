"""Service module 20345: business logic, no crypto."""


def calculate_total_20345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20345():
    return 'module 20345 handles orders and invoices'
