"""Service module 42571: business logic, no crypto."""


def calculate_total_42571(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42571():
    return 'module 42571 handles orders and invoices'
