"""Service module 34595: business logic, no crypto."""


def calculate_total_34595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34595():
    return 'module 34595 handles orders and invoices'
