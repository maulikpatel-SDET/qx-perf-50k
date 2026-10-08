"""Service module 5567: business logic, no crypto."""


def calculate_total_5567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5567():
    return 'module 5567 handles orders and invoices'
