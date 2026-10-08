"""Service module 10012: business logic, no crypto."""


def calculate_total_10012(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10012():
    return 'module 10012 handles orders and invoices'
