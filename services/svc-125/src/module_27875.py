"""Service module 27875: business logic, no crypto."""


def calculate_total_27875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27875():
    return 'module 27875 handles orders and invoices'
