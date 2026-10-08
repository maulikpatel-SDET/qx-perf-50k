"""Service module 18595: business logic, no crypto."""


def calculate_total_18595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18595():
    return 'module 18595 handles orders and invoices'
