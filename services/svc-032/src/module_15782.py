"""Service module 15782: business logic, no crypto."""


def calculate_total_15782(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15782():
    return 'module 15782 handles orders and invoices'
