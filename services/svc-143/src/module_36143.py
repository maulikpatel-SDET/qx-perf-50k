"""Service module 36143: business logic, no crypto."""


def calculate_total_36143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36143():
    return 'module 36143 handles orders and invoices'
