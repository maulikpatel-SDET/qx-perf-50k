"""Service module 34814: business logic, no crypto."""


def calculate_total_34814(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34814():
    return 'module 34814 handles orders and invoices'
