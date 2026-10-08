"""Service module 30618: business logic, no crypto."""


def calculate_total_30618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30618():
    return 'module 30618 handles orders and invoices'
