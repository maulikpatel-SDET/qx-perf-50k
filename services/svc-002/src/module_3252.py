"""Service module 3252: business logic, no crypto."""


def calculate_total_3252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3252():
    return 'module 3252 handles orders and invoices'
