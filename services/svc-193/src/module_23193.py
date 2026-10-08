"""Service module 23193: business logic, no crypto."""


def calculate_total_23193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23193():
    return 'module 23193 handles orders and invoices'
