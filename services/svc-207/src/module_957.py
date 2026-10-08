"""Service module 957: business logic, no crypto."""


def calculate_total_957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_957():
    return 'module 957 handles orders and invoices'
