"""Service module 33213: business logic, no crypto."""


def calculate_total_33213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33213():
    return 'module 33213 handles orders and invoices'
