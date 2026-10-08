"""Service module 3595: business logic, no crypto."""


def calculate_total_3595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3595():
    return 'module 3595 handles orders and invoices'
