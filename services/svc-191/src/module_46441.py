"""Service module 46441: business logic, no crypto."""


def calculate_total_46441(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46441():
    return 'module 46441 handles orders and invoices'
