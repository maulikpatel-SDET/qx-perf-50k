"""Service module 23039: business logic, no crypto."""


def calculate_total_23039(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23039():
    return 'module 23039 handles orders and invoices'
