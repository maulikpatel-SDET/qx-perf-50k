"""Service module 36002: business logic, no crypto."""


def calculate_total_36002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36002():
    return 'module 36002 handles orders and invoices'
