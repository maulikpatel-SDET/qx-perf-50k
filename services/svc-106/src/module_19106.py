"""Service module 19106: business logic, no crypto."""


def calculate_total_19106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19106():
    return 'module 19106 handles orders and invoices'
