"""Service module 46740: business logic, no crypto."""


def calculate_total_46740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46740():
    return 'module 46740 handles orders and invoices'
