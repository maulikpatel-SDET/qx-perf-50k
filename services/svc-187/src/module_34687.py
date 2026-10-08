"""Service module 34687: business logic, no crypto."""


def calculate_total_34687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34687():
    return 'module 34687 handles orders and invoices'
