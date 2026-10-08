"""Service module 37002: business logic, no crypto."""


def calculate_total_37002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37002():
    return 'module 37002 handles orders and invoices'
