"""Service module 18994: business logic, no crypto."""


def calculate_total_18994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18994():
    return 'module 18994 handles orders and invoices'
