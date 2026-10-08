"""Service module 38981: business logic, no crypto."""


def calculate_total_38981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38981():
    return 'module 38981 handles orders and invoices'
