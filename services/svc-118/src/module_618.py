"""Service module 618: business logic, no crypto."""


def calculate_total_618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_618():
    return 'module 618 handles orders and invoices'
