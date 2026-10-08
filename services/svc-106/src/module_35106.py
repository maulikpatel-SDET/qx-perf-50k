"""Service module 35106: business logic, no crypto."""


def calculate_total_35106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35106():
    return 'module 35106 handles orders and invoices'
