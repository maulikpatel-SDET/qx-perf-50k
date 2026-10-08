"""Service module 47907: business logic, no crypto."""


def calculate_total_47907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47907():
    return 'module 47907 handles orders and invoices'
