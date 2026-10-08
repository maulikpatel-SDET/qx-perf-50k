"""Service module 28618: business logic, no crypto."""


def calculate_total_28618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28618():
    return 'module 28618 handles orders and invoices'
