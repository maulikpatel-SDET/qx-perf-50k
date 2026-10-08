"""Service module 18053: business logic, no crypto."""


def calculate_total_18053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18053():
    return 'module 18053 handles orders and invoices'
