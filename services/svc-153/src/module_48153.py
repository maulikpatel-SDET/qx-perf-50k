"""Service module 48153: business logic, no crypto."""


def calculate_total_48153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48153():
    return 'module 48153 handles orders and invoices'
