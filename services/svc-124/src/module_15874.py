"""Service module 15874: business logic, no crypto."""


def calculate_total_15874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15874():
    return 'module 15874 handles orders and invoices'
