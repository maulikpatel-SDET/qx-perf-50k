"""Service module 34629: business logic, no crypto."""


def calculate_total_34629(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34629():
    return 'module 34629 handles orders and invoices'
