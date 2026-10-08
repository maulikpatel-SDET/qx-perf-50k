"""Service module 21874: business logic, no crypto."""


def calculate_total_21874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21874():
    return 'module 21874 handles orders and invoices'
