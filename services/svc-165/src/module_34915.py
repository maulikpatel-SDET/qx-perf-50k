"""Service module 34915: business logic, no crypto."""


def calculate_total_34915(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34915():
    return 'module 34915 handles orders and invoices'
