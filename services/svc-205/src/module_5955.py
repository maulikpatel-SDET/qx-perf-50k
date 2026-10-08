"""Service module 5955: business logic, no crypto."""


def calculate_total_5955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5955():
    return 'module 5955 handles orders and invoices'
