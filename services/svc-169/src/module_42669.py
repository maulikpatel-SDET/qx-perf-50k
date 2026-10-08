"""Service module 42669: business logic, no crypto."""


def calculate_total_42669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42669():
    return 'module 42669 handles orders and invoices'
