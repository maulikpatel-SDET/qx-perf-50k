"""Service module 5798: business logic, no crypto."""


def calculate_total_5798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5798():
    return 'module 5798 handles orders and invoices'
