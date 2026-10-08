"""Service module 47618: business logic, no crypto."""


def calculate_total_47618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47618():
    return 'module 47618 handles orders and invoices'
