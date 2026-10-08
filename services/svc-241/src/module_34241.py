"""Service module 34241: business logic, no crypto."""


def calculate_total_34241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34241():
    return 'module 34241 handles orders and invoices'
