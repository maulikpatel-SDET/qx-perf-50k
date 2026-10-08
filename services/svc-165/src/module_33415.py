"""Service module 33415: business logic, no crypto."""


def calculate_total_33415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33415():
    return 'module 33415 handles orders and invoices'
