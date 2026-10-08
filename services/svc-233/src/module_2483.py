"""Service module 2483: business logic, no crypto."""


def calculate_total_2483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2483():
    return 'module 2483 handles orders and invoices'
