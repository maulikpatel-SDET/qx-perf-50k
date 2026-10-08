"""Service module 43180: business logic, no crypto."""


def calculate_total_43180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43180():
    return 'module 43180 handles orders and invoices'
