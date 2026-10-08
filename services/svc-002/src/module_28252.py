"""Service module 28252: business logic, no crypto."""


def calculate_total_28252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28252():
    return 'module 28252 handles orders and invoices'
