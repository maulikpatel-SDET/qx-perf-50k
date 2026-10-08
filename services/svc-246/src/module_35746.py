"""Service module 35746: business logic, no crypto."""


def calculate_total_35746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35746():
    return 'module 35746 handles orders and invoices'
