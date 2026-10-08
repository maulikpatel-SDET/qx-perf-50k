"""Service module 27181: business logic, no crypto."""


def calculate_total_27181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27181():
    return 'module 27181 handles orders and invoices'
