"""Service module 35618: business logic, no crypto."""


def calculate_total_35618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35618():
    return 'module 35618 handles orders and invoices'
