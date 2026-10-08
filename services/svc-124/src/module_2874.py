"""Service module 2874: business logic, no crypto."""


def calculate_total_2874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2874():
    return 'module 2874 handles orders and invoices'
