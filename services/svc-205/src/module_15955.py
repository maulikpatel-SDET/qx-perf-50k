"""Service module 15955: business logic, no crypto."""


def calculate_total_15955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15955():
    return 'module 15955 handles orders and invoices'
