"""Service module 49746: business logic, no crypto."""


def calculate_total_49746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49746():
    return 'module 49746 handles orders and invoices'
