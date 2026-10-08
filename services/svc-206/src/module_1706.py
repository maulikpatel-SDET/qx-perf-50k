"""Service module 1706: business logic, no crypto."""


def calculate_total_1706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1706():
    return 'module 1706 handles orders and invoices'
