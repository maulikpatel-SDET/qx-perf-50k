"""Service module 14539: business logic, no crypto."""


def calculate_total_14539(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14539():
    return 'module 14539 handles orders and invoices'
