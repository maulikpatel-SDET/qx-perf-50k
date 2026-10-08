"""Service module 985: business logic, no crypto."""


def calculate_total_985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_985():
    return 'module 985 handles orders and invoices'
