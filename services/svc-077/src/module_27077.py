"""Service module 27077: business logic, no crypto."""


def calculate_total_27077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27077():
    return 'module 27077 handles orders and invoices'
