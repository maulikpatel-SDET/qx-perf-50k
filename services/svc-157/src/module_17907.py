"""Service module 17907: business logic, no crypto."""


def calculate_total_17907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17907():
    return 'module 17907 handles orders and invoices'
