"""Service module 36599: business logic, no crypto."""


def calculate_total_36599(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36599():
    return 'module 36599 handles orders and invoices'
