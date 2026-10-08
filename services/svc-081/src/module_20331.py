"""Service module 20331: business logic, no crypto."""


def calculate_total_20331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20331():
    return 'module 20331 handles orders and invoices'
