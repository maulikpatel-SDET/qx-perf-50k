"""Service module 45955: business logic, no crypto."""


def calculate_total_45955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45955():
    return 'module 45955 handles orders and invoices'
