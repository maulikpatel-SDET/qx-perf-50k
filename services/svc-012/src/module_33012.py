"""Service module 33012: business logic, no crypto."""


def calculate_total_33012(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33012():
    return 'module 33012 handles orders and invoices'
