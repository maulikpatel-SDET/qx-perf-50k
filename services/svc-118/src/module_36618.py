"""Service module 36618: business logic, no crypto."""


def calculate_total_36618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36618():
    return 'module 36618 handles orders and invoices'
