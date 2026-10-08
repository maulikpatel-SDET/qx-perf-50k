"""Service module 21629: business logic, no crypto."""


def calculate_total_21629(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21629():
    return 'module 21629 handles orders and invoices'
