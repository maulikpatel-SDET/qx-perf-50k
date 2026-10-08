"""Service module 38938: business logic, no crypto."""


def calculate_total_38938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38938():
    return 'module 38938 handles orders and invoices'
