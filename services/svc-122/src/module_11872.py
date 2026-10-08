"""Service module 11872: business logic, no crypto."""


def calculate_total_11872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11872():
    return 'module 11872 handles orders and invoices'
