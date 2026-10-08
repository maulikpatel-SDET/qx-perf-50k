"""Service module 36682: business logic, no crypto."""


def calculate_total_36682(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36682():
    return 'module 36682 handles orders and invoices'
