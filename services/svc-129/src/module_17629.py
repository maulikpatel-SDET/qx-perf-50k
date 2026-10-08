"""Service module 17629: business logic, no crypto."""


def calculate_total_17629(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17629():
    return 'module 17629 handles orders and invoices'
