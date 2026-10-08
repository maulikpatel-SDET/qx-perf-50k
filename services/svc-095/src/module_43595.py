"""Service module 43595: business logic, no crypto."""


def calculate_total_43595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43595():
    return 'module 43595 handles orders and invoices'
