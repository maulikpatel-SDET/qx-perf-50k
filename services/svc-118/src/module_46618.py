"""Service module 46618: business logic, no crypto."""


def calculate_total_46618(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46618():
    return 'module 46618 handles orders and invoices'
