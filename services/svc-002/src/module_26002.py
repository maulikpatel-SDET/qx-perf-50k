"""Service module 26002: business logic, no crypto."""


def calculate_total_26002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26002():
    return 'module 26002 handles orders and invoices'
