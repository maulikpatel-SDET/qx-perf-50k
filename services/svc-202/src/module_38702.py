"""Service module 38702: business logic, no crypto."""


def calculate_total_38702(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38702():
    return 'module 38702 handles orders and invoices'
