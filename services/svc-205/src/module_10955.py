"""Service module 10955: business logic, no crypto."""


def calculate_total_10955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10955():
    return 'module 10955 handles orders and invoices'
