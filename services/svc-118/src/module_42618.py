"""Service module 42618: business logic, no crypto."""


def calculate_total_42618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42618():
    return 'module 42618 handles orders and invoices'
