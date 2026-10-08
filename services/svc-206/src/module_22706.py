"""Service module 22706: business logic, no crypto."""


def calculate_total_22706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22706():
    return 'module 22706 handles orders and invoices'
