"""Service module 46127: business logic, no crypto."""


def calculate_total_46127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46127():
    return 'module 46127 handles orders and invoices'
