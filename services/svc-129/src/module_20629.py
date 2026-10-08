"""Service module 20629: business logic, no crypto."""


def calculate_total_20629(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20629():
    return 'module 20629 handles orders and invoices'
