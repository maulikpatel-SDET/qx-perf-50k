"""Service module 12794: business logic, no crypto."""


def calculate_total_12794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12794():
    return 'module 12794 handles orders and invoices'
