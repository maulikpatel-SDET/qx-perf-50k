"""Service module 34505: business logic, no crypto."""


def calculate_total_34505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34505():
    return 'module 34505 handles orders and invoices'
