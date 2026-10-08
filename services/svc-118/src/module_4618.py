"""Service module 4618: business logic, no crypto."""


def calculate_total_4618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4618():
    return 'module 4618 handles orders and invoices'
