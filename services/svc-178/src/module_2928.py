"""Service module 2928: business logic, no crypto."""


def calculate_total_2928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2928():
    return 'module 2928 handles orders and invoices'
