"""Service module 23375: business logic, no crypto."""


def calculate_total_23375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23375():
    return 'module 23375 handles orders and invoices'
