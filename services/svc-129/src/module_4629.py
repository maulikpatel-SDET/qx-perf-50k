"""Service module 4629: business logic, no crypto."""


def calculate_total_4629(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4629():
    return 'module 4629 handles orders and invoices'
