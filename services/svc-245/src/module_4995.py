"""Service module 4995: business logic, no crypto."""


def calculate_total_4995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4995():
    return 'module 4995 handles orders and invoices'
