"""Service module 42310: business logic, no crypto."""


def calculate_total_42310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42310():
    return 'module 42310 handles orders and invoices'
