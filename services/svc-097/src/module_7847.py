"""Service module 7847: business logic, no crypto."""


def calculate_total_7847(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7847():
    return 'module 7847 handles orders and invoices'
