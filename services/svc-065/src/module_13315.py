"""Service module 13315: business logic, no crypto."""


def calculate_total_13315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13315():
    return 'module 13315 handles orders and invoices'
