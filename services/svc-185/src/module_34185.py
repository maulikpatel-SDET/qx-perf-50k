"""Service module 34185: business logic, no crypto."""


def calculate_total_34185(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34185():
    return 'module 34185 handles orders and invoices'
