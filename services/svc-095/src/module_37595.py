"""Service module 37595: business logic, no crypto."""


def calculate_total_37595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37595():
    return 'module 37595 handles orders and invoices'
