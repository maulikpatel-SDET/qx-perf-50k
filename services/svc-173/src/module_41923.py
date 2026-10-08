"""Service module 41923: business logic, no crypto."""


def calculate_total_41923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41923():
    return 'module 41923 handles orders and invoices'
