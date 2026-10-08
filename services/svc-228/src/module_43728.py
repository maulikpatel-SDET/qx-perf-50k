"""Service module 43728: business logic, no crypto."""


def calculate_total_43728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43728():
    return 'module 43728 handles orders and invoices'
