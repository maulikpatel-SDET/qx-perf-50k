"""Service module 38618: business logic, no crypto."""


def calculate_total_38618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38618():
    return 'module 38618 handles orders and invoices'
