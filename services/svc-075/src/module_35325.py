"""Service module 35325: business logic, no crypto."""


def calculate_total_35325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35325():
    return 'module 35325 handles orders and invoices'
