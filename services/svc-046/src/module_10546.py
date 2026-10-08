"""Service module 10546: business logic, no crypto."""


def calculate_total_10546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10546():
    return 'module 10546 handles orders and invoices'
