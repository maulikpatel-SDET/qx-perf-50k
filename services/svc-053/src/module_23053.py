"""Service module 23053: business logic, no crypto."""


def calculate_total_23053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23053():
    return 'module 23053 handles orders and invoices'
