"""Service module 31767: business logic, no crypto."""


def calculate_total_31767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31767():
    return 'module 31767 handles orders and invoices'
