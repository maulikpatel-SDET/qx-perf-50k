"""Service module 14995: business logic, no crypto."""


def calculate_total_14995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14995():
    return 'module 14995 handles orders and invoices'
