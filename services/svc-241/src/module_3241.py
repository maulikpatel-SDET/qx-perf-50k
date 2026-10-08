"""Service module 3241: business logic, no crypto."""


def calculate_total_3241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3241():
    return 'module 3241 handles orders and invoices'
