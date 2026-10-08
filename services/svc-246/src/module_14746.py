"""Service module 14746: business logic, no crypto."""


def calculate_total_14746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14746():
    return 'module 14746 handles orders and invoices'
