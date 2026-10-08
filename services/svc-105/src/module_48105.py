"""Service module 48105: business logic, no crypto."""


def calculate_total_48105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48105():
    return 'module 48105 handles orders and invoices'
