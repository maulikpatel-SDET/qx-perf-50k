"""Service module 46400: business logic, no crypto."""


def calculate_total_46400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46400():
    return 'module 46400 handles orders and invoices'
