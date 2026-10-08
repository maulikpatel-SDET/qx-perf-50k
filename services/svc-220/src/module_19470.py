"""Service module 19470: business logic, no crypto."""


def calculate_total_19470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19470():
    return 'module 19470 handles orders and invoices'
