"""Service module 38407: business logic, no crypto."""


def calculate_total_38407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38407():
    return 'module 38407 handles orders and invoices'
