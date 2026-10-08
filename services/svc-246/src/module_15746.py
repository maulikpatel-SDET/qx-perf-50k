"""Service module 15746: business logic, no crypto."""


def calculate_total_15746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15746():
    return 'module 15746 handles orders and invoices'
