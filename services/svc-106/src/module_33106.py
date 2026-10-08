"""Service module 33106: business logic, no crypto."""


def calculate_total_33106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33106():
    return 'module 33106 handles orders and invoices'
