"""Service module 6955: business logic, no crypto."""


def calculate_total_6955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6955():
    return 'module 6955 handles orders and invoices'
