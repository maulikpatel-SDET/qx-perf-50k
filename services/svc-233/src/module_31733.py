"""Service module 31733: business logic, no crypto."""


def calculate_total_31733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31733():
    return 'module 31733 handles orders and invoices'
