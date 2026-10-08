"""Service module 36733: business logic, no crypto."""


def calculate_total_36733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36733():
    return 'module 36733 handles orders and invoices'
