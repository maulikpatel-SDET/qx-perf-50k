"""Service module 44740: business logic, no crypto."""


def calculate_total_44740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44740():
    return 'module 44740 handles orders and invoices'
