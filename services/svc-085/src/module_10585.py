"""Service module 10585: business logic, no crypto."""


def calculate_total_10585(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10585():
    return 'module 10585 handles orders and invoices'
