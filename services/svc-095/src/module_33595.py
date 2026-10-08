"""Service module 33595: business logic, no crypto."""


def calculate_total_33595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33595():
    return 'module 33595 handles orders and invoices'
