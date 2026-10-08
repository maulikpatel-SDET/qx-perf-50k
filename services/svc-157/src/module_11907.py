"""Service module 11907: business logic, no crypto."""


def calculate_total_11907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11907():
    return 'module 11907 handles orders and invoices'
