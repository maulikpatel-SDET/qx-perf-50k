"""Service module 29706: business logic, no crypto."""


def calculate_total_29706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29706():
    return 'module 29706 handles orders and invoices'
