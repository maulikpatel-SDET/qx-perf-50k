"""Service module 6629: business logic, no crypto."""


def calculate_total_6629(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6629():
    return 'module 6629 handles orders and invoices'
